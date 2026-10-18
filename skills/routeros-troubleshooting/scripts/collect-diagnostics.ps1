<#
.SYNOPSIS
    Collects a read-only triage bundle from a RouterOS device over SSH into one text file.

.DESCRIPTION
    Runs only print and monitor commands (resources, packages, interfaces, addresses, routes, DNS, services,
    the memory log, a five-second CPU profile) and changes nothing on the router.
    Authentication uses your SSH key or agent (BatchMode), so no password is read or stored.
    Needs the OpenSSH client (ssh) in the PATH, which Windows 10 and later include.
    A command the router rejects (for example health on a model without sensors) is noted in the file and
    the run continues. The file holds addresses, routes and log lines of your network: share it only with
    people who should see them. For MikroTik support use /system/sup-output instead.

.PARAMETER HostName
    Router address or name.

.PARAMETER User
    Login name. Default: admin.

.PARAMETER Port
    SSH port. Default: 22.

.PARAMETER Identity
    Private key file to use. Default: your SSH agent or default keys.

.PARAMETER OutDirectory
    Folder for the file. Default: the current directory.

.PARAMETER NoProfile
    Skip the five-second CPU profile.

.EXAMPLE
    ./collect-diagnostics.ps1 -HostName 192.0.2.1 -User admin -OutDirectory ./diag
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory)]
    [string]$HostName,

    [string]$User = 'admin',
    [int]$Port = 22,
    [string]$Identity,
    [string]$OutDirectory = '.',
    [switch]$NoProfile
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$commands = @(
    '/system/identity/print'
    '/system/resource/print'
    '/system/routerboard/print'
    '/system/package/print'
    '/system/clock/print'
    '/system/health/print'
    '/interface/print'
    '/ip/address/print'
    '/ip/route/print'
    '/ip/dns/print'
    '/ip/service/print'
    '/ip/firewall/connection/print count-only'
    '/log/print'
)
if (-not $NoProfile) { $commands += '/tool/profile cpu=all duration=5s' }

$baseArguments = @('-p', $Port, '-o', 'BatchMode=yes', '-o', 'ConnectTimeout=15')
if ($Identity) { $baseArguments += @('-i', $Identity) }

$null = New-Item -ItemType Directory -Force -Path $OutDirectory
$safeName = $HostName -replace '[^A-Za-z0-9._-]', '_'
$file = Join-Path (Resolve-Path -LiteralPath $OutDirectory).Path ("{0}-diag-{1}.txt" -f $safeName, (Get-Date -Format 'yyyyMMdd-HHmmss'))

$sections = foreach ($command in $commands) {
    $output = & ssh @baseArguments "$User@$HostName" $command 2>&1
    $failed = $LASTEXITCODE -ne 0
    $body = (($output | ForEach-Object { "$_" }) -join "`n") -replace "`r", ''
    [pscustomobject]@{ Header = "### $command"; Body = $body; Failed = $failed }
}

$failedCount = @($sections | Where-Object { $_.Failed }).Count
if ($failedCount -eq $commands.Count) {
    throw 'Every command failed (check the host, the user and your SSH key).'
}
if (-not (@($sections | Where-Object { $_.Body }).Count)) {
    throw 'The router returned no output.'
}

$text = ($sections | ForEach-Object {
        $suffix = if ($_.Failed) { "`n(command failed)" } else { '' }
        "{0}`n{1}{2}`n" -f $_.Header, $_.Body, $suffix
    }) -join "`n"
[System.IO.File]::WriteAllText($file, $text, (New-Object System.Text.UTF8Encoding($false)))
Write-Output ("saved {0} lines to {1} ({2} command(s) failed)" -f ([regex]::Matches($text, "`n").Count), $file, $failedCount)
