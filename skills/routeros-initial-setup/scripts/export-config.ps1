<#
.SYNOPSIS
    Saves the configuration of a RouterOS device as a timestamped .rsc file over SSH.

.DESCRIPTION
    Read-only: runs "/export" on the router and writes the output to a local file.
    Authentication uses your SSH key or agent (BatchMode), so no password is read or stored.
    Needs the OpenSSH client (ssh) in the PATH, which Windows 10 and later include.

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

.PARAMETER Terse
    One full command per line, easier to compare with a diff tool.

.PARAMETER ShowSensitive
    Include passwords and keys in the export. Treat the file like a password.

.EXAMPLE
    ./export-config.ps1 -HostName 192.0.2.1 -User admin -OutDirectory ./backups
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory)]
    [string]$HostName,

    [string]$User = 'admin',
    [int]$Port = 22,
    [string]$Identity,
    [string]$OutDirectory = '.',
    [switch]$Terse,
    [switch]$ShowSensitive
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$command = '/export'
if ($Terse) { $command += ' terse' }
if ($ShowSensitive) {
    $command += ' show-sensitive'
    Write-Warning 'The export will contain passwords and keys; keep the file private.'
}

$sshArguments = @('-p', $Port, '-o', 'BatchMode=yes', '-o', 'ConnectTimeout=15')
if ($Identity) { $sshArguments += @('-i', $Identity) }
$sshArguments += @("$User@$HostName", $command)

$null = New-Item -ItemType Directory -Force -Path $OutDirectory
$safeName = $HostName -replace '[^A-Za-z0-9._-]', '_'
$file = Join-Path (Resolve-Path -LiteralPath $OutDirectory).Path ("{0}-{1}.rsc" -f $safeName, (Get-Date -Format 'yyyyMMdd-HHmmss'))

$output = & ssh @sshArguments
if ($LASTEXITCODE -ne 0 -or -not $output) {
    throw 'The export failed or was empty (check the host, the user and your SSH key).'
}

# RouterOS ends lines with CR LF; write plain LF so that the file diffs cleanly.
$text = (($output -join "`n") -replace "`r", '') + "`n"
[System.IO.File]::WriteAllText($file, $text, (New-Object System.Text.UTF8Encoding($false)))
Write-Output ("saved {0} lines to {1}" -f [regex]::Matches($text, "`n").Count, $file)
