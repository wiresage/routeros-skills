<#
.SYNOPSIS
    Installs the RouterOS skills into the folder an AI agent reads skills from.

.DESCRIPTION
    Skills are plain folders, so installing is a copy (or a symbolic link with -Link).
    Examples of target folders: Claude Code ~\.claude\skills, Codex ~\.agents\skills,
    Copilot .github\skills. Check your agent's documentation; these locations change.

.PARAMETER Target
    Folder that your agent reads skills from. Created if it does not exist.

.PARAMETER Skill
    Names of the skills to install. Default: every skill.

.PARAMETER Link
    Create symbolic links instead of copies, so that "git pull" updates the installed skills.
    Creating symbolic links on Windows needs Developer Mode or an elevated prompt.

.PARAMETER Force
    Replace a skill that is already installed.

.PARAMETER List
    Print the available skills and exit.

.EXAMPLE
    scripts\install-skills.ps1 -Target "$HOME\.claude\skills"

.EXAMPLE
    scripts\install-skills.ps1 -Target .agents\skills -Skill routeros-firewall, routeros-vpn -Link
#>
[CmdletBinding(SupportsShouldProcess)]
param(
    [Parameter(Position = 0)]
    [string]$Target,

    [Parameter(Position = 1, ValueFromRemainingArguments)]
    [string[]]$Skill,

    [switch]$Link,
    [switch]$Force,
    [switch]$List
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$repoRoot = Split-Path -Parent $PSScriptRoot
$skillsDir = Join-Path $repoRoot 'skills'

function Get-SkillName {
    Get-ChildItem -LiteralPath $skillsDir -Directory |
        Where-Object { Test-Path -LiteralPath (Join-Path $_.FullName 'SKILL.md') } |
        ForEach-Object { $_.Name }
}

if ($List) {
    Get-SkillName
    return
}

if (-not $Target) {
    throw 'Target is required, for example: -Target "$HOME\.claude\skills"'
}

$selected = if ($Skill) { $Skill } else { @(Get-SkillName) }
$null = New-Item -ItemType Directory -Force -Path $Target
$resolvedTarget = (Resolve-Path -LiteralPath $Target).Path

$installed = 0
foreach ($name in $selected) {
    $source = Join-Path $skillsDir $name
    if (-not (Test-Path -LiteralPath (Join-Path $source 'SKILL.md'))) {
        throw "No such skill: $name (use -List)"
    }
    $destination = Join-Path $resolvedTarget $name
    if (Test-Path -LiteralPath $destination) {
        if (-not $Force) {
            Write-Output "skip: $destination already exists (use -Force to replace it)"
            continue
        }
        if ($PSCmdlet.ShouldProcess($destination, 'Remove the installed skill')) {
            Remove-Item -LiteralPath $destination -Recurse -Force
        }
    }
    if (-not $PSCmdlet.ShouldProcess($destination, 'Install skill')) {
        continue
    }
    if ($Link) {
        $null = New-Item -ItemType SymbolicLink -Path $destination -Target $source
        Write-Output "linked: $destination -> $source"
    }
    else {
        Copy-Item -LiteralPath $source -Destination $destination -Recurse
        Write-Output "copied: $destination"
    }
    $installed++
}

Write-Output "installed $installed skill(s) into $resolvedTarget"
