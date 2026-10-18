#!/usr/bin/env python3
"""Call the RouterOS REST API from the command line (standard library only).

    ROUTEROS_PASSWORD=... rest_call.py --host 192.168.88.1 --user monitoring --ca rest-ca.crt \\
        GET /system/resource --query .proplist=board-name,cpu-load
    rest_call.py --host 192.168.88.1 --user admin --ca rest-ca.crt \\
        PUT /ip/firewall/address-list --data '{"list":"blocked","address":"203.0.113.45","timeout":"1d"}'
    rest_call.py --host 192.168.88.1 --user monitoring --ca rest-ca.crt \\
        POST /interface/monitor-traffic --data '{"interface":"ether1","once":""}'

The method maps to a console command: GET print, PUT add, PATCH set, DELETE remove, POST any command.
The path is the console path with slashes (``/ip/address``, ``/ip/address/*1``). Reserved characters other than
the ``*`` of an id must be percent-encoded by you (``/file/flash%2Fbackup.rsc``).

The password is read from the ROUTEROS_PASSWORD environment variable, or asked for on a terminal. It is never taken
from the command line, so it does not end up in shell history or process lists. HTTPS is the default and the
certificate is verified (with ``--ca`` for your own authority). The router ends any request after 60 seconds, so
bound commands such as ping with ``count`` and monitor commands with ``once``.

Exit status: 0 success, 1 the router answered with an error (the body is printed to stderr), 2 bad usage,
3 connection or certificate failure.
"""

from __future__ import annotations

import argparse
import base64
import getpass
import json
import os
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

METHODS = ("GET", "PUT", "PATCH", "POST", "DELETE")


def build_url(host: str, port: int | None, path: str, query: list[str], plain_http: bool) -> str:
    """Return the full REST URL; query items are ``key=value`` pairs for GET filters and ``.proplist``."""
    if not path.startswith("/"):
        raise ValueError("the path must start with /")
    scheme = "http" if plain_http else "https"
    netloc = f"{host}:{port}" if port else host
    # Keep the asterisk of record ids and existing percent escapes; encode everything else that is unsafe.
    url = f"{scheme}://{netloc}/rest{urllib.parse.quote(path, safe='/*%')}"
    if query:
        pairs = []
        for item in query:
            key, separator, value = item.partition("=")
            if not separator:
                raise ValueError(f"query item {item!r} must look like key=value")
            pairs.append((key, value))
        url += "?" + urllib.parse.urlencode(pairs, safe=",.*")
    return url


def load_body(data: str | None) -> bytes | None:
    """Parse ``--data`` (a JSON string or ``@file``) and return the request body."""
    if data is None:
        return None
    text = Path(data[1:]).read_text(encoding="utf-8") if data.startswith("@") else data
    return json.dumps(json.loads(text)).encode("utf-8")


def make_context(ca: str | None, insecure: bool) -> ssl.SSLContext:
    if insecure:
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        return context
    return ssl.create_default_context(cafile=ca)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("method", choices=METHODS, type=str.upper, help="HTTP method (GET, PUT, PATCH, POST, DELETE)")
    parser.add_argument("path", help="console path, for example /ip/address or /ip/address/*1")
    parser.add_argument("--host", required=True, help="router address or name, as named in its certificate")
    parser.add_argument("--port", type=int, help="port of the web service (default 443, or 80 with --plain-http)")
    parser.add_argument("--user", default="admin", help="REST user (default: admin)")
    parser.add_argument("--ca", help="PEM file with the certificate authority that signed the router certificate")
    parser.add_argument("--insecure", action="store_true", help="do not verify the certificate (testing only)")
    parser.add_argument("--plain-http", action="store_true", help="use HTTP: the password travels unencrypted")
    parser.add_argument("--query", action="append", default=[], metavar="KEY=VALUE", help="URL parameter (repeatable)")
    parser.add_argument("--data", help="JSON body, or @file to read it from a file")
    parser.add_argument("--timeout", type=float, default=70.0, help="seconds to wait for the reply (default: 70)")
    args = parser.parse_args()

    password = os.environ.get("ROUTEROS_PASSWORD")
    if password is None:
        if not sys.stdin.isatty():
            print("error: set ROUTEROS_PASSWORD (the password is never read from arguments)", file=sys.stderr)
            return 2
        password = getpass.getpass(f"Password for {args.user}@{args.host}: ")

    try:
        url = build_url(args.host, args.port, args.path, args.query, args.plain_http)
        body = load_body(args.data)
    except (ValueError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.plain_http:
        print("warning: plain HTTP sends the password unencrypted", file=sys.stderr)
    if args.insecure:
        print("warning: certificate verification is off", file=sys.stderr)

    credentials = base64.b64encode(f"{args.user}:{password}".encode()).decode("ascii")
    headers = {"Authorization": f"Basic {credentials}", "Accept": "application/json"}
    if body is not None:
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(url, data=body, method=args.method, headers=headers)
    context = None if args.plain_http else make_context(args.ca, args.insecure)

    try:
        with urllib.request.urlopen(request, timeout=args.timeout, context=context) as response:
            payload = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        print(f"HTTP {exc.code} {exc.reason}", file=sys.stderr)
        print(exc.read().decode("utf-8", errors="replace"), file=sys.stderr)
        return 1
    except (urllib.error.URLError, ssl.SSLError, TimeoutError, OSError) as exc:
        print(f"error: could not reach {args.host}: {exc}", file=sys.stderr)
        return 3

    if payload:
        try:
            print(json.dumps(json.loads(payload), indent=2, ensure_ascii=False))
        except json.JSONDecodeError:
            print(payload)
    return 0


if __name__ == "__main__":
    sys.exit(main())
