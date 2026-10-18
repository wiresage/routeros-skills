#!/usr/bin/env bash
# Save the configuration of a RouterOS device as a timestamped .rsc file over SSH.
#
#   export-config.sh --host 192.0.2.1 --user admin --out ./backups
#
# Read-only: it runs "/export" on the router and writes the output to a local file.
# Authentication uses your SSH key or agent (BatchMode), so no password is read or stored.
set -euo pipefail

usage() {
    cat <<'EOF'
Usage: export-config.sh --host HOST [--user USER] [--port PORT] [--identity KEYFILE]
                        [--out DIR] [--terse] [--show-sensitive]

  --host HOST         router address or name (required)
  --user USER         login name (default: admin)
  --port PORT         SSH port (default: 22)
  --identity KEYFILE  private key to use (default: your SSH agent or default keys)
  --out DIR           folder for the file (default: current directory)
  --terse             one full command per line, easier to compare with diff
  --show-sensitive    include passwords and keys; the file is then created with mode 600
  -h, --help          show this help

The file is named HOST-YYYYmmdd-HHMMSS.rsc. Without --show-sensitive, RouterOS leaves passwords
and private keys out. Treat a file made with --show-sensitive like a password.
EOF
}

host=""
user="admin"
port="22"
identity=""
out="."
terse=0
sensitive=0

while [ $# -gt 0 ]; do
    case "$1" in
        --host) host="${2:?--host needs a value}"; shift 2 ;;
        --user) user="${2:?--user needs a value}"; shift 2 ;;
        --port) port="${2:?--port needs a value}"; shift 2 ;;
        --identity) identity="${2:?--identity needs a value}"; shift 2 ;;
        --out) out="${2:?--out needs a value}"; shift 2 ;;
        --terse) terse=1; shift ;;
        --show-sensitive) sensitive=1; shift ;;
        -h | --help) usage; exit 0 ;;
        *) echo "error: unknown argument $1" >&2; usage >&2; exit 2 ;;
    esac
done

if [ -z "$host" ]; then
    echo "error: --host is required" >&2
    usage >&2
    exit 2
fi

command="/export"
[ "$terse" -eq 1 ] && command="$command terse"
[ "$sensitive" -eq 1 ] && command="$command show-sensitive"

ssh_args=(-p "$port" -o BatchMode=yes -o ConnectTimeout=15)
[ -n "$identity" ] && ssh_args+=(-i "$identity")

mkdir -p "$out"
file="$out/${host//[^A-Za-z0-9._-]/_}-$(date +%Y%m%d-%H%M%S).rsc"

if [ "$sensitive" -eq 1 ]; then
    umask 077
    echo "warning: the export will contain passwords and keys; keep $file private" >&2
fi

# The command string is built from fixed words above, so expanding it on the client side is intended.
# shellcheck disable=SC2029
if ! ssh "${ssh_args[@]}" "$user@$host" "$command" | tr -d '\r' >"$file"; then
    rm -f -- "$file"
    echo "error: the export failed (check the host, the user and your SSH key)" >&2
    exit 1
fi

if [ ! -s "$file" ]; then
    rm -f -- "$file"
    echo "error: the router returned an empty export" >&2
    exit 1
fi

echo "saved $(wc -l <"$file" | tr -d ' ') lines to $file"
