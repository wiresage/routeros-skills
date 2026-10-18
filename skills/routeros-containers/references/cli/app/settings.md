# /app/settings

> Source: https://manual.mikrotik.com/docs/cli-reference/app/settings

Syscap: app; Package: container; Type: Settings Directory

**Arguments**

- `disk` (enum: none): Global setting that specifies which disk will be used for storage operations
- `router-ip` (ipAddr): Manually specifies the IP address at which the current RouterOS device can be reached
- `lan-bridge` (iface_enum { none }): Manually specifies the bridge interface that represents the local area network
- `media-path` (file): Manually specifies the directory path where all media files will be stored
- `download-path` (file): Manually specifies the directory path where all downloaded content will be stored
- `show-in-webfig` (bool): Controls whether links to enabled applications are displayed on the WebFig login page
- `auto-update` (bool): Global setting that enables automatic updates for all installed applications packages
- `registry-mirrors` (multi { array-id, array-id, src-and-dst: composite { src: string , dst: string } }): Specifies one or more registry mirror URLs for container image retrieval
- `app-store-urls` (multi { array-id, app-store-url: string }): URL to a custom app store. Must point to a YAML array where each application is an element

**Read-only arguments**

- `assumed-router-ip` (ipAddr): Automatically detected network IP address of the RouterOS device
- `assumed-lan-bridge` (iface_enum { none }): Automatically detected bridge interface used for LAN connectivity
- `assumed-media-path` (file): Default media storage path, typically located on the system disk
- `assumed-download-path` (file): Default download directory path, typically located within the media storage area
- `certificate-status` (string)
- `certificate` (enum: none)
