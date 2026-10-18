# /ip/media/settings

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/media/settings

Conditions: !smips; Type: Settings Directory

Settings shared by all DLNA media servers in [`/ip/media`](../media.md). See [DLNA Media Server](../../../guides/storage/dlna.md).

**Arguments**

- `thumbnails` (string): Comma separated list of filenames (should end with .jpg). If name of a file in a directory matches any filename in the list, that file is treated as a thumbnail to any media file in that directory: it is no longer listed as a picture, and players show it as the cover picture of the other files. See [DLNA Media Server](../../../guides/storage/dlna.md). Default: empty.
