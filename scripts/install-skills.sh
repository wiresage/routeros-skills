#!/usr/bin/env bash
# Install the RouterOS skills into the folder an AI agent reads skills from.
#
#   scripts/install-skills.sh --target ~/.claude/skills
#   scripts/install-skills.sh --target .agents/skills --link routeros-firewall routeros-vpn
#
# Skills are plain folders, so installing is a copy (or a symlink with --link).
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
skills_dir="$repo_root/skills"

usage() {
    cat <<'EOF'
Usage: install-skills.sh --target DIR [--link] [--force] [SKILL...]
       install-skills.sh --list

Options:
  --target DIR  folder that your agent reads skills from (created if missing)
  --link        symlink the skills instead of copying them, so "git pull" updates them
  --force       replace a skill that is already installed
  --list        print the available skills and exit
  -h, --help    show this help

With no SKILL names, every skill is installed. Examples of target folders:
  Claude Code   ~/.claude/skills or .claude/skills
  Codex         ~/.agents/skills or .agents/skills
  Copilot       .github/skills
Check your agent's documentation; these locations change.
EOF
}

list_skills() {
    local dir
    for dir in "$skills_dir"/*/; do
        [ -f "${dir}SKILL.md" ] && basename "$dir"
    done
}

target=""
link=0
force=0
selected=()

while [ $# -gt 0 ]; do
    case "$1" in
        --target)
            [ $# -ge 2 ] || { echo "error: --target needs a folder" >&2; exit 2; }
            target="$2"
            shift 2
            ;;
        --link) link=1; shift ;;
        --force) force=1; shift ;;
        --list) list_skills; exit 0 ;;
        -h | --help) usage; exit 0 ;;
        -*) echo "error: unknown option $1" >&2; usage >&2; exit 2 ;;
        *) selected+=("$1"); shift ;;
    esac
done

if [ -z "$target" ]; then
    echo "error: --target is required" >&2
    usage >&2
    exit 2
fi

if [ ${#selected[@]} -eq 0 ]; then
    while IFS= read -r name; do selected+=("$name"); done < <(list_skills)
fi

mkdir -p "$target"
target="$(cd "$target" && pwd)"

installed=0
for name in "${selected[@]}"; do
    source_dir="$skills_dir/$name"
    if [ ! -f "$source_dir/SKILL.md" ]; then
        echo "error: no such skill: $name (see --list)" >&2
        exit 1
    fi
    destination="$target/$name"
    if [ -e "$destination" ] || [ -L "$destination" ]; then
        if [ "$force" -ne 1 ]; then
            echo "skip: $destination already exists (use --force to replace it)"
            continue
        fi
        rm -rf -- "${destination:?}"
    fi
    if [ "$link" -eq 1 ]; then
        ln -s "$source_dir" "$destination"
        echo "linked: $destination -> $source_dir"
    else
        cp -R "$source_dir" "$destination"
        echo "copied: $destination"
    fi
    installed=$((installed + 1))
done

echo "installed $installed skill(s) into $target"
