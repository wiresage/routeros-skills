#!/usr/bin/env python3
"""Crawl help.mikrotik.com/docs into a local cache.

help.mikrotik.com is a Confluence site. Its documentation is frozen: the manual at
manual.mikrotik.com replaced it, but some pages (quick guides, user manuals, the
knowledge base and a few reference pages) never moved. This script downloads every
page of the documentation spaces through Confluence's public REST API so that the
gaps can be found and filled.

robots.txt on the site asks for a 5 second crawl delay, so requests are sequential
and spaced accordingly; each request returns several pages with their bodies.

    python tools/crawl_help.py crawl  --cache .cache/help
    python tools/crawl_help.py verify --cache .cache/help
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

BASE = "https://help.mikrotik.com/docs"
USER_AGENT = "routeros-skills-crawler/1.0 (+https://github.com/wiresage/routeros-skills)"
CRAWL_DELAY = 5.0
# ROS: RouterOS, RKB: knowledge base, SWOS: SwOS, QG: quick guides, UM: user manuals, WEB: general guides.
SPACES = ["ROS", "RKB", "SWOS", "WEB", "QG", "UM"]
EXPAND = "body.export_view,version,ancestors,metadata.labels"


class CrawlError(RuntimeError):
    """A request failed after all retries."""


def get_json(url: str, retries: int = 4) -> dict:
    last: Exception | None = None
    for attempt in range(retries):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
            with urllib.request.urlopen(request, timeout=120) as response:
                return json.loads(response.read().decode("utf-8"))
        except (urllib.error.URLError, TimeoutError, ConnectionError, json.JSONDecodeError) as exc:
            last = exc
            time.sleep(CRAWL_DELAY * (attempt + 2))
    raise CrawlError(f"giving up on {url}: {last}")


def space_total(space: str) -> int:
    query = urllib.parse.urlencode({"cql": f'space="{space}" and type=page', "limit": 1})
    return int(get_json(f"{BASE}/rest/api/search?{query}")["totalSize"])


def crawl(cache: Path, spaces: list[str], page_size: int) -> int:
    cache.mkdir(parents=True, exist_ok=True)
    total = 0
    for space in spaces:
        start = 0
        count = 0
        while True:
            query = urllib.parse.urlencode(
                {"spaceKey": space, "type": "page", "limit": page_size, "start": start, "expand": EXPAND}
            )
            data = get_json(f"{BASE}/rest/api/content?{query}")
            for page in data["results"]:
                record = {
                    "id": page["id"],
                    "space": space,
                    "title": page["title"],
                    "url": BASE + page["_links"]["webui"],
                    "version": page["version"]["number"],
                    "modified": page["version"]["when"],
                    "ancestors": [a["title"] for a in page.get("ancestors", [])],
                    "labels": [lbl["name"] for lbl in page.get("metadata", {}).get("labels", {}).get("results", [])],
                    "html": page["body"]["export_view"]["value"],
                }
                destination = cache / f"{space}-{page['id']}.json"
                destination.write_text(json.dumps(record, ensure_ascii=False), encoding="utf-8")
                count += 1
            print(f"{space}: {count} pages", flush=True)
            if "next" not in data["_links"] or not data["results"]:
                break
            start += page_size
            time.sleep(CRAWL_DELAY)
        total += count
        time.sleep(CRAWL_DELAY)
    print(f"downloaded {total} pages")
    return 0


def verify(cache: Path, spaces: list[str]) -> int:
    """Compare the number of cached pages per space with what the server reports."""
    problems = 0
    for space in spaces:
        have = len(list(cache.glob(f"{space}-*.json")))
        want = space_total(space)
        status = "ok" if have == want else "MISMATCH"
        print(f"{space}: {have} cached, {want} on the server: {status}")
        problems += have != want
        time.sleep(CRAWL_DELAY)
    empty = [p.name for p in cache.glob("*.json") if not json.loads(p.read_text(encoding="utf-8"))["html"].strip()]
    print(f"pages with an empty body: {len(empty)} (navigation pages are expected to be nearly empty)")
    print("OK" if problems == 0 else f"{problems} space(s) differ")
    return 1 if problems else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("command", choices=["crawl", "verify"])
    parser.add_argument("--cache", type=Path, default=Path(".cache/help"))
    parser.add_argument("--spaces", nargs="*", default=SPACES)
    parser.add_argument("--page-size", type=int, default=10)
    args = parser.parse_args()
    if args.command == "crawl":
        return crawl(args.cache, args.spaces, args.page_size)
    return verify(args.cache, args.spaces)


if __name__ == "__main__":
    sys.exit(main())
