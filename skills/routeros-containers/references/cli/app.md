# /app

> Source: https://manual.mikrotik.com/docs/cli-reference/app

Syscap: app; Package: container; Type: Directory

## Commands

### /app/cleanup

Syscap: app; Package: container; Type: Command

Removes all application data, configuration files, and the container image. This operation is destructive and irreversible.

### /app/remove

Syscap: app; Package: container; Type: Command

Removes the specified application from the system.

### /app/restart

Syscap: app; Package: container; Type: Command

### /app/setup

Syscap: app; Package: container; Type: Command

Starts the setup wizard that automates networking, storage, and registry configuration for the App system.

**Read-only arguments**

- `disk` (enum: none): Selected storage disk for application installation
- `lan-bridge` (iface_enum { none }): Selected LAN bridge interface for container networking
- `router-ip-alt` (alt { router-ip-enum: enum , router-ip: ipAddr }): Manual IP address override for the RouterOS device

### /app/update

Syscap: app; Package: container; Type: Command

Updates the specified application to the latest available container image.
