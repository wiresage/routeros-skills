<#
.SYNOPSIS
    Checks a RouterOS script file (.rsc) on a real router without applying it.

.DESCRIPTION
    Uploads the file with scp under a temporary name, runs "/import ... verbose=yes dry-run" (which reads
    every line and reports syntax errors but makes no configuration change), prints the router's report and
    removes the temporary file again. Authentication uses your SSH key or agent (BatchMode), so no password
    is read or stored. Needs the OpenSSH client (ssh and scp) in the PATH, which Windows 10 and later include.

    A dry run catches syntax errors and unknown commands or parameters as the importer sees them; it cannot
    prove that the commands succeed at run time (missing interfaces, duplicate entries, permissions).

    Exit status: 0 no errors found, 1 the router reported errors, 3 upload or connection failed.

.PARAMETER Path
    The .rsc file to check.

.PARAMETER HostName
    Router address or name.

.PARAMETER User
    Login name. Default: admin.

.PARAMETER Port
    SSH port. Default: 22.

.PARAMETER Identity
    Private key file to use. Default: your SSH agent or default keys.

.EXAMPLE
    ./dry-run-import.ps1 -HostName 192.0.2.1 -User admin my-config.rsc
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory, Position = 0)]
    [string]$Path,

    [Parameter(Mandatory)]
    [string]$HostName,

    [string]$User = 'admin',
    [int]$Port = 22,
    [string]$Identity
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Invoke-Native {
    # Runs an external command and returns its exit code and combined output. Stderr text is collected as plain
    # text: with ErrorActionPreference Stop, Windows PowerShell 5.1 would turn it into a terminating error.
    param([string]$FilePath, [string[]]$Arguments)
    $previous = $ErrorActionPreference
    $ErrorActionPreference = 'Continue'
    try {
        $lines = & $FilePath @Arguments 2>&1
        $code = $LASTEXITCODE
    }
    finally {
        $ErrorActionPreference = $previous
    }
    [pscustomobject]@{
        ExitCode = $code
        Output   = (($lines | ForEach-Object { "$_" }) -join "`n") -replace "`r", ''
    }
}

if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
    $host.UI.WriteErrorLine("error: $Path not found")
    exit 2
}

$options = @('-o', 'BatchMode=yes', '-o', 'ConnectTimeout=15')
if ($Identity) { $options += @('-i', $Identity) }
$target = "$User@$HostName"
$remote = 'dryrun-{0}.rsc' -f (Get-Random)

try {
    $upload = Invoke-Native -FilePath 'scp' -Arguments (@('-P', "$Port") + $options + @((Resolve-Path -LiteralPath $Path).Path, "${target}:$remote"))
    if ($upload.ExitCode -ne 0) {
        $host.UI.WriteErrorLine("error: could not upload $Path (check the host, the user, your SSH key and that SSH is enabled)")
        exit 3
    }

    $check = Invoke-Native -FilePath 'ssh' -Arguments (@('-p', "$Port") + $options + @($target, "/import file-name=$remote verbose=yes dry-run"))
    $output = $check.Output
    if (-not $output) {
        $host.UI.WriteErrorLine('error: the router did not answer')
        exit 3
    }
    Write-Output $output

    $pattern = 'Script Error:|error\(s\) in import file|bad command name|\(line \d+ column \d+\)'
    if ($output -match $pattern) {
        $host.UI.WriteErrorLine("dry run found errors in $Path")
        exit 1
    }
    Write-Output "dry run found no errors in $Path"
}
finally {
    # Best effort: the file may not exist when the upload failed.
    $null = Invoke-Native -FilePath 'ssh' -Arguments (@('-p', "$Port") + $options + @($target, "/file/remove $remote"))
}
