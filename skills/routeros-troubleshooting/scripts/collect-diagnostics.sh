#!/usr/bin/env bash
# Collect a read-only triage bundle from a RouterOS device over SSH into one text file.
#
#   collect-diagnostics.sh --host 192.0.2.1 --user admin --out ./diag
#
# It runs only print and monitor commands (resources, packages, interfaces, addresses, routes, DNS, services,
# the memory log, a five-second CPU profile) and changes nothing on the router.
# Authentication uses your SSH key or agent (BatchMode), so no password is read or stored.
set -euo pipefail

usage() {
    cat <<'EOF'
Usage: collect-diagnostics.sh --host HOST [--user USER] [--port PORT] [--identity KEYFILE]
                              [--out DIR] [--no-profile]

  --host HOST         router address or name (required)
  --user USER         login name (default: admin)
  --port PORT         SSH port (default: 22)
  --identity KEYFILE  private key to use (default: your SSH agent or default keys)
  --out DIR           folder for the file (default: current directory)
  --no-profile        skip the five-second CPU profile
  -h, --help          show this help

The file is named HOST-diag-YYYYmmdd-HHMMSS.txt. A command the router rejects (for example health on a
model without sensors) is noted in the file and the run continues. The file holds addresses, routes and log
lines of your network: share it only with people who should see them. For MikroTik support use
/system/sup-output instead.
EOF
}

host=""
user="admin"
port="22"
identity=""
out="."
profile=1

while [ $# -gt 0 ]; do
    case "$1" in
        --host) host="${2:?--host needs a value}"; shift 2 ;;
        --user) user="${2:?--user needs a value}"; shift 2 ;;
        --port) port="${2:?--port needs a value}"; shift 2 ;;
        --identity) identity="${2:?--identity needs a value}"; shift 2 ;;
        --out) out="${2:?--out needs a value}"; shift 2 ;;
        --no-profile) profile=0; shift ;;
        -h | --help) usage; exit 0 ;;
        *) echo "error: unknown argument $1" >&2; usage >&2; exit 2 ;;
    esac
done

if [ -z "$host" ]; then
    echo "error: --host is required" >&2
    usage >&2
    exit 2
fi

commands=(
    "/system/identity/print"
    "/system/resource/print"
    "/system/routerboard/print"
    "/system/package/print"
    "/system/clock/print"
    "/system/health/print"
    "/interface/print"
    "/ip/address/print"
    "/ip/route/print"
    "/ip/dns/print"
    "/ip/service/print"
    "/ip/firewall/connection/print count-only"
    '/log/print'
)
[ "$profile" -eq 1 ] && commands+=("/tool/profile cpu=all duration=5s")

ssh_args=(-p "$port" -o BatchMode=yes -o ConnectTimeout=15)
[ -n "$identity" ] && ssh_args+=(-i "$identity")

mkdir -p "$out"
file="$out/${host//[^A-Za-z0-9._-]/_}-diag-$(date +%Y%m%d-%H%M%S).txt"
: >"$file"

failed=0
for command in "${commands[@]}"; do
    printf '### %s\n' "$command" >>"$file"
    # The commands are fixed strings from the list above, so expanding them on the client side is intended.
    # shellcheck disable=SC2029
    if ! ssh "${ssh_args[@]}" "$user@$host" "$command" 2>&1 | tr -d '\r' >>"$file"; then
        echo "(command failed)" >>"$file"
        failed=$((failed + 1))
    fi
    printf '\n' >>"$file"
done

# With pipefail a failed ssh fails the pipeline, so every command failing means no router could be reached.
if [ "$failed" -eq "${#commands[@]}" ]; then
    rm -f -- "$file"
    echo "error: every command failed (check the host, the user and your SSH key)" >&2
    exit 1
fi

if ! grep -qv -e '^###' -e '^$' "$file"; then
    rm -f -- "$file"
    echo "error: the router returned no output" >&2
    exit 1
fi

echo "saved $(wc -l <"$file" | tr -d ' ') lines to $file ($failed command(s) failed)"
