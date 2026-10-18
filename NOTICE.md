# Notice

## MikroTik documentation

The files under `skills/*/references/` are converted copies of the RouterOS documentation published by MikroTik at
<https://manual.mikrotik.com> and, for pages the manual does not have, at <https://help.mikrotik.com/docs>.

- The documentation is copyright MikroTik (SIA Mikrotikls). It is **not** covered by this repository's MIT license.
- MikroTik publishes the manual in machine-readable form on purpose (`/llms.txt`, `/llms-full.txt`, a Markdown copy of
  every page) and its `robots.txt` allows AI crawlers. The crawlers in `tools/` identify themselves, respect the
  `Crawl-delay` of help.mikrotik.com and read only public pages.
- Every converted page starts with a `Source:` line that links to the original. Treat the original as authoritative; the
  copies are a snapshot (see `docs-snapshot.json`) and may be out of date.
- Conversion changes the format, not the wording: MDX components become Markdown, links are rewritten, pictures are
  replaced by a `[Figure]` note, and internal numeric enum codes are omitted from the CLI reference.

Before this repository is made public, confirm that MikroTik's terms allow redistributing these copies, or switch the
references to download-on-demand (`tools/build_references.py` can regenerate them locally from the sources).

## Trademarks

MikroTik, RouterOS, RouterBOARD, WinBox and SwOS are trademarks of MikroTik. This project is not affiliated with or
endorsed by MikroTik.
