#!/usr/bin/env python3
"""Print the newest RouterOS version of each release channel and compare it with a version you have.

    check_latest_version.py                       # every channel of RouterOS 7
    check_latest_version.py --channel stable --current 7.23.1
    check_latest_version.py --series 6 --json

The version numbers come from https://upgrade.mikrotik.com, the server a router asks when you run
"/system/package/update/check-for-updates". The URL scheme (NEWESTa7.<channel>, NEWEST6.<channel>) is observed
behaviour, not documented by MikroTik, so treat a failure as "could not check" rather than "no update".
Read-only: it makes one HTTPS GET request per channel and verifies the server certificate.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

BASE = "https://upgrade.mikrotik.com/routeros"
CHANNELS = ("long-term", "stable", "testing", "development")
FILE_PREFIX = {"7": "NEWESTa7", "6": "NEWEST6"}
VERSION = re.compile(r"^(\d+)\.(\d+)(?:\.(\d+))?(?:(beta|rc)(\d+))?$")
STAGE_RANK = {"beta": 0, "rc": 1, None: 2}


def parse_version(text: str) -> tuple[int, int, int, int, int]:
    """Sortable form of a RouterOS version: 7.26beta1 < 7.25rc2 < 7.25 < 7.25.1."""
    match = VERSION.match(text.strip())
    if not match:
        raise ValueError(f"not a RouterOS version: {text!r}")
    major, minor, patch, stage, number = match.groups()
    return int(major), int(minor), int(patch or 0), STAGE_RANK[stage], int(number or 0)


def fetch_newest(series: str, channel: str, timeout: float) -> tuple[str, datetime]:
    url = f"{BASE}/{FILE_PREFIX[series]}.{channel}"
    request = urllib.request.Request(url, headers={"User-Agent": "routeros-skills/check_latest_version"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        body = response.read().decode("ascii", "replace").split()
    if len(body) != 2 or not body[1].isdigit():
        raise ValueError(f"unexpected answer from {url}: {' '.join(body)[:80]!r}")
    return body[0], datetime.fromtimestamp(int(body[1]), tz=timezone.utc)


def main() -> int:
    parser = argparse.ArgumentParser(description="Show the newest RouterOS version per release channel.")
    parser.add_argument("--series", choices=sorted(FILE_PREFIX), default="7", help="major version line (default: 7)")
    parser.add_argument("--channel", choices=CHANNELS, action="append", help="channel to query (default: all)")
    parser.add_argument("--current", help="your version, for example 7.23.1; reports whether it is older")
    parser.add_argument("--timeout", type=float, default=15.0, help="seconds to wait for the server (default: 15)")
    parser.add_argument("--json", action="store_true", help="print JSON instead of text")
    args = parser.parse_args()

    try:
        current = parse_version(args.current) if args.current else None
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    results = []
    failed = False
    for channel in args.channel or CHANNELS:
        try:
            version, released = fetch_newest(args.series, channel, args.timeout)
        except (urllib.error.URLError, TimeoutError, ValueError) as exc:
            print(f"error: {channel}: {exc}", file=sys.stderr)
            failed = True
            continue
        entry = {"channel": channel, "version": version, "released": released.strftime("%Y-%m-%d")}
        if current is not None:
            entry["newer_than_current"] = parse_version(version) > current
        results.append(entry)

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        for entry in results:
            line = f"{entry['channel']:<12} {entry['version']:<12} {entry['released']}"
            if "newer_than_current" in entry:
                line += "  newer than yours" if entry["newer_than_current"] else "  not newer than yours"
            print(line)
    return 1 if failed or not results else 0


if __name__ == "__main__":
    sys.exit(main())
