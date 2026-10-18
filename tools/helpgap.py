"""Decide, for every help.mikrotik.com page, whether the manual already covers it.

The help site is frozen and the manual replaced it. A help page is

* ``imported``  : listed under a skill's ``help`` in scopes.json (the manual has nothing equivalent);
* ``excluded``  : listed in ``excluded_help`` (navigation pages, or not RouterOS documentation);
* ``covered``   : the manual has the same page. Decided by an identical title, by at least half of its
                  six-word phrases appearing in the manual, or by an explicit entry in ``covered_help``;
* ``unclassified`` : none of the above. The build stops until someone decides.
"""

from __future__ import annotations

import re

from bs4 import BeautifulSoup

SHINGLE = 6
OVERLAP = 0.5
IMPORTED_SPACES = {"QG"}


def normalise(text: str) -> str:
    return " ".join(re.sub(r"[^a-z0-9 ]+", " ", text.lower()).split())


def compact(text: str) -> str:
    """Title key that ignores case, spaces and punctuation (``hAP ac²`` and ``hap-ac2`` match)."""
    return re.sub(r"[^a-z0-9]+", "", text.lower())


def shingles(text: str, size: int = SHINGLE) -> set[str]:
    words = normalise(text).split()
    return {" ".join(words[i : i + size]) for i in range(max(0, len(words) - size + 1))}


def classify(
    help_pages: dict[str, dict],
    manual_titles: set[str],
    manual_corpus: set[str],
    imported: set[str],
    excluded: dict[str, str],
    covered: dict[str, str],
) -> dict[str, tuple[str, str]]:
    """Return ``{page id: (status, detail)}`` for every crawled help page."""
    result: dict[str, tuple[str, str]] = {}
    for page_id, page in help_pages.items():
        space = page["space"]
        if page_id in imported or space in IMPORTED_SPACES:
            result[page_id] = ("imported", "")
        elif page_id in excluded or space in excluded:
            result[page_id] = ("excluded", excluded.get(page_id) or excluded[space])
        elif page_id in covered:
            result[page_id] = ("covered", covered[page_id])
        elif compact(page["title"]) in manual_titles:
            result[page_id] = ("covered", "same title in the manual")
        else:
            text = BeautifulSoup(page["html"], "lxml").get_text(" ", strip=True)
            phrases = shingles(text)
            share = len(phrases & manual_corpus) / len(phrases) if phrases else 1.0
            if share >= OVERLAP:
                result[page_id] = ("covered", f"{share:.0%} of its text is in the manual")
            else:
                result[page_id] = ("unclassified", f"{share:.0%} of its text is in the manual")
    return result
