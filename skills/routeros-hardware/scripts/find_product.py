#!/usr/bin/env python3
"""Search the MikroTik product manuals in ``references/products/`` by model name, category or keyword.

    find_product.py hap ac
    find_product.py --category "LTE products" sim
    find_product.py --grep "passive poe" --limit 5
    find_product.py --list-categories

Every term must appear (case-insensitive) in the product title, file name or manual text. Output lists the title,
category and file for each match; ``--grep`` also prints the matching lines. Standard library only.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

PRODUCTS = Path(__file__).resolve().parent.parent / "references" / "products"
CATEGORY = re.compile(r"^> Category:\s*(.+?)\s*$", re.MULTILINE)
TITLE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)


@dataclass
class Product:
    path: Path
    title: str
    category: str
    text: str

    def haystack(self) -> str:
        return f"{self.title}\n{self.path.stem}\n{self.text}".lower()


def load_products(directory: Path = PRODUCTS) -> list[Product]:
    products = []
    for path in sorted(directory.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        title = TITLE.search(text)
        category = CATEGORY.search(text)
        products.append(
            Product(path, title.group(1) if title else path.stem, category.group(1) if category else "", text)
        )
    return products


def search(
    products: list[Product], terms: list[str], category: str | None = None, grep: str | None = None
) -> list[Product]:
    wanted = [t.lower() for t in terms]
    hits = []
    for product in products:
        if category and category.lower() not in product.category.lower():
            continue
        haystack = product.haystack()
        if not all(t in haystack for t in wanted):
            continue
        if grep and grep.lower() not in haystack:
            continue
        hits.append(product)
    # Matches in the title or file name come first: they are the models the user most likely means.
    hits.sort(key=lambda p: (not all(t in f"{p.title} {p.path.stem}".lower() for t in wanted), p.title.lower()))
    return hits


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("terms", nargs="*", help="words that must all appear in the title, file name or text")
    parser.add_argument("--category", help="only products whose category contains this text")
    parser.add_argument("--grep", help="also require this phrase and print the lines that contain it")
    parser.add_argument("--limit", type=int, default=20, help="maximum number of products to list (default: 20)")
    parser.add_argument("--list-categories", action="store_true", help="list the categories with their product counts")
    args = parser.parse_args()

    # Manuals contain symbols that a legacy Windows code page cannot print.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    if not PRODUCTS.is_dir():
        print(f"error: {PRODUCTS} not found", file=sys.stderr)
        return 1
    products = load_products()

    if args.list_categories:
        counts: dict[str, int] = {}
        for product in products:
            counts[product.category or "(none)"] = counts.get(product.category or "(none)", 0) + 1
        for name, count in sorted(counts.items(), key=lambda item: (-item[1], item[0])):
            print(f"{count:4d}  {name}")
        return 0

    if not args.terms and not args.category and not args.grep:
        parser.print_usage(sys.stderr)
        print("error: give at least one search term, --category or --grep", file=sys.stderr)
        return 2

    hits = search(products, args.terms, args.category, args.grep)
    if not hits:
        print("no matching product")
        return 1
    for product in hits[: args.limit]:
        relative = product.path.relative_to(PRODUCTS.parent.parent).as_posix()
        print(f"{product.title}  [{product.category}]  {relative}")
        if args.grep:
            needle = args.grep.lower()
            for line in product.text.splitlines():
                if needle in line.lower():
                    print(f"    {line.strip()[:200]}")
    if len(hits) > args.limit:
        print(f"... {len(hits) - args.limit} more; narrow the search or raise --limit")
    return 0


if __name__ == "__main__":
    sys.exit(main())
