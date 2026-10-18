# /ip/cloud/back-to-home-file

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/cloud/back-to-home-file

Syscap: cloud-vpn; Type: Directory

Directories and files shared with File Share. Each share gets a secret link under `<serial>.routingthecloud.net`, and the service runs while at least one share exists. For examples, see [File Share](../../../guides/network-management/cloud/file-share.md). The service state is in [`settings`](back-to-home-file/settings.md).

**Flags**

- `X` (disabled): The share is disabled, and its link returns HTTP 404.
- `I` (invalid): The share cannot be served yet, for example while the router requests the certificate. A comment line shows the reason, such as `getting cert status: requesting SSL certificate`.
- `D`: dynamic

**Arguments**

- `path` (file): Directory or file to share, as `/file/print` shows it, for example `usb1/photos`. The router shows it with a leading `/`.
- `allow-uploads` (bool): Whether visitors of a directory share can upload files and create folders in it. Without it, the router refuses uploads with HTTP 403. Default: no.
- `expires` (alt { expires: enum (never) { never:0xFFFFFFFF } , interval: time , date-time: date }): When the share stops working: `never`, a date and time such as `"2026-10-01 00:00:00"`, or a time interval such as `1h`. The router converts an interval to a date. `never` keeps the share until you remove it.

**Read-only arguments**

- `key` (string): Random key of the share, the last part of `url`.
- `url` (string): Link to the share page, `https://<serial>.routingthecloud.net/s/<key>`. A directory share lists its files; anyone who has the link can open it.
- `direct-url` (string): `url` with `?dl`. It downloads the shared file, or the whole directory as `download.zip`.
- `downloads` (num): Number of direct downloads of the share. Opening the share page does not count.
