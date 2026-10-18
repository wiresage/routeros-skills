#!/usr/bin/env python3
"""Crawl manual.mikrotik.com into a local cache.

The manual is a Docusaurus site that publishes its own machine-readable copy:

* ``/llms.txt`` lists every documentation page together with the URL of its
  Markdown source (narrative pages and the whole CLI reference).
* ``/sitemap.xml`` lists every rendered HTML page, including the hardware
  manuals, which exist only as HTML.

This script downloads the Markdown page for every ``llms.txt`` entry and the
rendered article for every hardware manual, then cross-checks the result
against the sitemap.

    python tools/crawl_manual.py crawl   --cache .cache/manual
    python tools/crawl_manual.py verify  --cache .cache/manual
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from bs4 import BeautifulSoup

BASE = "https://manual.mikrotik.com"
USER_AGENT = "routeros-skills-crawler/1.0 (+https://github.com/wiresage/routeros-skills)"
ENTRY = re.compile(r"^- \[(?P<title>.*?)\]\((?P<url>https://manual\.mikrotik\.com/[^)]+)\)(?::\s*(?P<desc>.*))?$")
# Sitemap areas that are not RouterOS documentation: blog posts, the documentation
# edit log, and tag listing pages (which only repeat links to existing pages).
SITEMAP_SKIP = ("docs/tags", "blog", "changelog")


class FetchError(RuntimeError):
    """A page could not be downloaded after all retries."""


def fetch(url: str, retries: int = 4) -> tuple[int, bytes]:
    """Return ``(status, body)``; 404 and 410 are results, anything else is retried."""
    last: Exception | None = None
    for attempt in range(retries):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(request, timeout=60) as response:
                return response.status, response.read()
        except urllib.error.HTTPError as exc:
            if exc.code in (404, 410):
                return exc.code, b""
            last = exc
        except (urllib.error.URLError, TimeoutError, ConnectionError) as exc:
            last = exc
        time.sleep(1.5 * (attempt + 1))
    raise FetchError(f"giving up on {url}: {last}")


def parse_index(text: str) -> list[dict]:
    """Parse ``llms.txt`` into entries, remembering the section each belongs to."""
    section = ""
    entries = []
    for line in text.splitlines():
        if line.startswith("## "):
            section = line[3:].strip()
            continue
        match = ENTRY.match(line)
        if match:
            entries.append(
                {
                    "title": match["title"],
                    "url": match["url"],
                    "description": (match["desc"] or "").strip(),
                    "section": section,
                }
            )
    return entries


def parse_sitemap(xml: str) -> list[str]:
    return re.findall(r"<loc>([^<]+)</loc>", xml)


def sitemap_path(url: str) -> str:
    return url[len(BASE) :].strip("/")


def hardware_urls(sitemap: list[str]) -> list[str]:
    """Hardware manual pages, without the ``/hardware/`` landing page itself."""
    return [u for u in sitemap if sitemap_path(u).startswith("hardware/")]


def extract_hardware(url: str, html: str) -> dict:
    """Keep the article body, title and breadcrumb of a rendered hardware manual."""
    soup = BeautifulSoup(html, "lxml")
    article = soup.find("article")
    if article is None:
        raise FetchError(f"no <article> in {url}")
    crumbs = [a.get_text(" ", strip=True) for a in soup.select("nav[aria-label='Breadcrumbs'] li")]
    heading = article.find("h1")
    return {
        "url": url,
        "title": heading.get_text(" ", strip=True) if heading else url.rstrip("/").rsplit("/", 1)[-1],
        "breadcrumbs": [c for c in crumbs if c],
        "html": str(article),
    }


def crawl(cache: Path, workers: int) -> int:
    pages_dir = cache / "pages"
    hardware_dir = cache / "hardware"
    pages_dir.mkdir(parents=True, exist_ok=True)
    hardware_dir.mkdir(parents=True, exist_ok=True)

    status, body = fetch(f"{BASE}/llms.txt")
    if status != 200:
        raise FetchError(f"llms.txt returned {status}")
    (cache / "llms.txt").write_bytes(body)
    entries = parse_index(body.decode("utf-8"))

    status, body = fetch(f"{BASE}/sitemap.xml")
    if status != 200:
        raise FetchError(f"sitemap.xml returned {status}")
    (cache / "sitemap.xml").write_bytes(body)
    sitemap = parse_sitemap(body.decode("utf-8"))

    status, body = fetch(f"{BASE}/llms-full.txt")
    if status == 200:
        (cache / "llms-full.txt").write_bytes(body)

    def download_page(entry: dict) -> dict:
        rel = entry["url"][len(BASE) + 1 :]
        status, data = fetch(entry["url"])
        record = {**entry, "path": rel, "status": status, "bytes": len(data)}
        if status == 200:
            destination = pages_dir / rel
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(data)
            record["sha256"] = hashlib.sha256(data).hexdigest()
        return record

    def download_hardware(url: str) -> dict:
        slug = sitemap_path(url)[len("hardware/") :]
        status, data = fetch(url if url.endswith("/") else url + "/")
        record = {"url": url, "path": f"hardware/{slug}.json", "status": status, "bytes": len(data)}
        if status == 200:
            page = extract_hardware(url, data.decode("utf-8"))
            (hardware_dir / f"{slug}.json").write_text(json.dumps(page, ensure_ascii=False), encoding="utf-8")
            record["title"] = page["title"]
            record["sha256"] = hashlib.sha256(data).hexdigest()
        return record

    hardware = hardware_urls(sitemap)
    print(f"llms.txt entries: {len(entries)}; hardware manuals: {len(hardware)}", flush=True)
    with ThreadPoolExecutor(max_workers=workers) as pool:
        pages = sorted(pool.map(download_page, entries), key=lambda r: r["path"])
        manuals = sorted(pool.map(download_hardware, hardware), key=lambda r: r["path"])

    manifest = {
        "source": BASE,
        "crawled": time.strftime("%Y-%m-%d", time.gmtime()),
        "pages": pages,
        "hardware": manuals,
    }
    (cache / "manifest.json").write_text(json.dumps(manifest, indent=1, ensure_ascii=False), encoding="utf-8")
    failed = [r for r in pages + manuals if r["status"] != 200]
    print(f"downloaded {len(pages) + len(manuals) - len(failed)} pages, {len(failed)} failed")
    for record in failed[:20]:
        print(f"  FAIL {record['status']} {record['url']}")
    return 1 if failed else 0


def verify(cache: Path) -> int:
    """Check the cache against the sitemap and the single-file corpus."""
    manifest = json.loads((cache / "manifest.json").read_text(encoding="utf-8"))
    pages = manifest["pages"]
    problems = 0

    indexed = {r["url"] for r in pages}
    sitemap = parse_sitemap((cache / "sitemap.xml").read_text(encoding="utf-8"))
    skipped = 0
    uncovered = []
    for url in sitemap:
        path = sitemap_path(url)
        if path.startswith(SITEMAP_SKIP) or path.startswith("hardware"):
            skipped += 1
            continue
        candidates = {f"{BASE}/{path}.md", f"{BASE}/{path}/index.md"}
        if path in ("", "docs"):
            candidates.add(f"{BASE}/docs/introduction.md")
        if not candidates & indexed:
            uncovered.append(url)
    print(f"sitemap: {len(sitemap)} URLs, {skipped} out of scope, {len(uncovered)} without a Markdown copy")
    for url in uncovered:
        print(f"  uncovered: {url}")
    problems += len(uncovered)

    failed = [r for r in pages + manifest["hardware"] if r["status"] != 200]
    print(f"downloads: {len(failed)} failed")
    problems += len(failed)

    mojibake = 0
    for record in pages:
        text = (cache / "pages" / record["path"]).read_text(encoding="utf-8")
        if "â€" in text or "�" in text:
            mojibake += 1
            print(f"  encoding damage: {record['path']}")
    print(f"encoding: {mojibake} pages with damaged characters")
    problems += mojibake

    corpus_file = cache / "llms-full.txt"
    if corpus_file.exists():
        corpus = re.sub(r"\s+", " ", corpus_file.read_text(encoding="utf-8"))
        absent = 0
        checked = 0
        for record in pages:
            text = (cache / "pages" / record["path"]).read_text(encoding="utf-8")
            body = re.sub(r"^# .*?\n+(> .*?\n+)?", "", text, count=1, flags=re.S)
            body = re.sub(r"^-+\s*\n", "", body.lstrip())
            probe = re.sub(r"\s+", " ", body.strip())[:120]
            if len(probe) < 40:
                continue
            checked += 1
            absent += probe not in corpus
        # llms-full.txt is formatted differently from the per-page copies, so this is informational only.
        print(f"llms-full.txt: {checked - absent}/{checked} page openings found")

    hardware_ok = sum(1 for r in manifest["hardware"] if r["status"] == 200)
    print(f"hardware manuals: {hardware_ok}/{len(manifest['hardware'])} downloaded")
    print("OK" if problems == 0 else f"{problems} problem(s)")
    return 1 if problems else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("command", choices=["crawl", "verify"])
    parser.add_argument("--cache", type=Path, default=Path(".cache/manual"))
    parser.add_argument("--workers", type=int, default=8)
    args = parser.parse_args()
    if args.command == "crawl":
        return crawl(args.cache, args.workers)
    return verify(args.cache)


if __name__ == "__main__":
    sys.exit(main())
