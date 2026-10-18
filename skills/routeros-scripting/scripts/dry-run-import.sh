#!/usr/bin/env bash
# Check a RouterOS script file (.rsc) on a real router without applying it.
#
#   dry-run-import.sh --host 192.0.2.1 --user admin my-config.rsc
#
# It uploads the file with scp under a temporary name, runs "/import ... verbose=yes dry-run" (which
# reads every line and reports syntax errors but makes no configuration change), prints the router's
# report and removes the temporary file again. Authentication uses your SSH key or agent (BatchMode),
# so no password is read or stored.
#
# Exit status: 0 no errors found, 1 the router reported errors, 2 bad usage, 3 upload or connection failed.
# A dry run catches syntax errors and unknown commands or parameters as the importer sees them; it cannot
# prove that the commands succeed at run time (missing interfaces, duplicate entries, permissions).
set -euo pipefail

usage() {
    cat <<'EOF'
Usage: dry-run-import.sh --host HOST [--user USER] [--port PORT] [--identity KEYFILE] FILE.rsc

  --host HOST         router address or name (required)
  --user USER         login name (default: admin)
  --port PORT         SSH port (default: 22)
  --identity KEYFILE  private key to use (default: your SSH agent or default keys)
  -h, --help          show this help

FILE.rsc is uploaded as dryrun-<random>.rsc, checked with "verbose=yes dry-run" and deleted afterwards.
The router needs the SSH service enabled; the user needs write and policy rights to import.
EOF
}

host=""
user="admin"
port="22"
identity=""
file=""

while [ $# -gt 0 ]; do
    case "$1" in
        --host) host="${2:?--host needs a value}"; shift 2 ;;
        --user) user="${2:?--user needs a value}"; shift 2 ;;
        --port) port="${2:?--port needs a value}"; shift 2 ;;
        --identity) identity="${2:?--identity needs a value}"; shift 2 ;;
        -h | --help) usage; exit 0 ;;
        -*) echo "error: unknown argument $1" >&2; usage >&2; exit 2 ;;
        *) file="$1"; shift ;;
    esac
done

if [ -z "$host" ] || [ -z "$file" ]; then
    echo "error: --host and a script file are required" >&2
    usage >&2
    exit 2
fi
if [ ! -f "$file" ]; then
    echo "error: $file not found" >&2
    exit 2
fi

ssh_options=(-o BatchMode=yes -o ConnectTimeout=15)
[ -n "$identity" ] && ssh_options+=(-i "$identity")

remote="dryrun-$$-${RANDOM}.rsc"

cleanup() {
    # Best effort: the file may not exist when the upload failed.
    ssh -p "$port" "${ssh_options[@]}" "$user@$host" "/file/remove $remote" >/dev/null 2>&1 || true
}
trap cleanup EXIT

if ! scp -P "$port" "${ssh_options[@]}" "$file" "$user@$host:$remote" >/dev/null; then
    echo "error: could not upload $file (check the host, the user, your SSH key and that SSH is enabled)" >&2
    exit 3
fi

# The command is built from a generated file name, so expanding it on the client side is intended.
# shellcheck disable=SC2029
if ! output=$(ssh -p "$port" "${ssh_options[@]}" "$user@$host" "/import file-name=$remote verbose=yes dry-run" 2>&1); then
    status=$?
    # RouterOS may also end the session with a non-zero status when the script has errors; the report decides.
    if [ -z "$output" ]; then
        echo "error: the router did not answer (ssh exit status $status)" >&2
        exit 3
    fi
fi
output=$(printf '%s\n' "$output" | tr -d '\r')
printf '%s\n' "$output"

if printf '%s\n' "$output" | grep -Eq 'Script Error:|error\(s\) in import file|bad command name|\(line [0-9]+ column [0-9]+\)'; then
    echo "dry run found errors in $file" >&2
    exit 1
fi
echo "dry run found no errors in $file"
