# /system/device-mode

> Source: https://manual.mikrotik.com/docs/cli-reference/system/device-mode

Type: Settings Directory

Current device-mode settings. The mode and the per-feature switches apply at startup and can be changed only with [`update`](device-mode.md), which requires physical confirmation. See the [Device mode](../../guides/system-information-and-utilities/device-mode.md) guide.

**Read-only arguments**

- `mode` (enum): Current device mode.
  - `advanced` - For CCR and 1100 series devices; previously called `enterprise`.
  - `basic` - For most other devices.
  - `home` - For home routers.
  - `rose` - For RDS and similar devices with wide disk use.
- `allowed-versions` (string): Comma-separated list of RouterOS versions considered secure, used to block downgrades to vulnerable releases (for example `7.13+,6.49.8+`). An upgrade to a release that ships a newer list updates it; a downgrade does not. Ignored when `install-any-version` is enabled.
- `flagged` (bool): Whether the device is in the flagged state: the startup configuration analysis found signs of unauthorized access and disabled the suspicious configuration. Reviewed and cleared with `update flagged=no`.
- `flagging-enabled` (bool): Whether the configuration analysis for signs of unauthorized access runs at startup. Default: yes.
- `scheduler` (bool): Whether `/system/scheduler` is allowed to perform actions.
- `socks` (bool): Whether the SOCKS proxy in `/ip/socks` is allowed.
- `fetch` (bool): Whether `/tool/fetch` is allowed.
- `pptp` (bool): Whether `/interface/pptp-client` and `/interface/pptp-server` are allowed.
- `l2tp` (bool): Whether `/interface/l2tp-client` and `/interface/l2tp-server` are allowed.
- `bandwidth-test` (bool): Whether `/tool/bandwidth-test`, `/tool/bandwidth-server` and `/tool/speed-test` are allowed.
- `traffic-gen` (bool): Whether `/tool/traffic-generator`, `/tool/flood-ping` and `/tool/ping-speed` are allowed.
- `sniffer` (bool): Whether `/tool/sniffer` is allowed.
- `ipsec` (bool): Whether `/ip/ipsec` is allowed.
- `romon` (bool): Whether `/tool/romon` is allowed.
- `proxy` (bool): Whether the web proxy in `/ip/proxy` is allowed.
- `hotspot` (bool): Whether `/ip/hotspot` is allowed.
- `smb` (bool): Whether `/ip/smb` is allowed.
- `email` (bool): Whether `/tool/e-mail` is allowed.
- `zerotier` (bool): Whether `/zerotier` is allowed.
- `container` (bool): Whether container functionality (`/container`) is allowed.
- `install-any-version` (bool): Whether installing RouterOS versions outside the `allowed-versions` list is permitted.
- `partitions` (bool): Whether changing the partition count (`/partitions`) is allowed.
- `routerboard` (bool): Whether changing `/system/routerboard/settings` options (except auto-upgrade) and the SwOS/RouterOS transition on dual-boot devices is allowed.
- `attempt-count` (num): Number of unsuccessful device-mode update attempts since the last reset; a request that cancels a pending update does not count. After three, an `update` is refused and a reset window opens for the time set by the last `activation-timeout`; a button press or power cycle inside the window resets the counter. A confirmed update also resets it. Default: 0.

## Commands

### /system/device-mode/update

Type: Command

Starts a device-mode configuration change. The change activates after a button press or power cycle and reboots the device; if it is not confirmed within `activation-timeout`, it is canceled. A regular reboot also cancels it. Running `update` without parameters cancels a pending update; an `update` with parameters while another is pending cancels the pending one and is not applied itself. See the [Device mode](../../guides/system-information-and-utilities/device-mode.md) guide.

**Arguments**

- `mode` (enum): Device mode to apply. Specifying `mode` replaces the entire device-mode configuration except the other parameters given in the same command; omitted features get the new mode's defaults.
  - `advanced` - Previously called `enterprise`.
  - `basic` - For most other devices.
  - `home` - For home routers.
  - `rose` - For RDS and similar devices with wide disk use.
- `flagged` (bool): Set to `no` to clear the flagged state, after inspecting the configuration for unauthorized changes. Requires physical confirmation.
- `flagging-enabled` (bool): Enable or disable the configuration analysis for signs of unauthorized access. Default: yes.
- `scheduler` (bool): Allow or block `/system/scheduler`.
- `socks` (bool): Allow or block `/ip/socks`.
- `fetch` (bool): Allow or block `/tool/fetch`.
- `pptp` (bool): Allow or block PPTP client and server interfaces.
- `l2tp` (bool): Allow or block L2TP client and server interfaces.
- `bandwidth-test` (bool): Allow or block `/tool/bandwidth-test`, `/tool/bandwidth-server` and `/tool/speed-test`.
- `traffic-gen` (bool): Allow or block `/tool/traffic-generator`, `/tool/flood-ping`, and `/tool/ping-speed`.
- `sniffer` (bool): Allow or block `/tool/sniffer`.
- `ipsec` (bool): Allow or block `/ip/ipsec`.
- `romon` (bool): Allow or block `/tool/romon`.
- `proxy` (bool): Allow or block `/ip/proxy`.
- `hotspot` (bool): Allow or block `/ip/hotspot`.
- `smb` (bool): Allow or block `/ip/smb`.
- `email` (bool): Allow or block `/tool/e-mail`.
- `zerotier` (bool): Allow or block `/zerotier`.
- `container` (bool): Allow or block container functionality.
- `install-any-version` (bool): Allow or block downgrading to RouterOS versions outside the allowed-versions list.
- `partitions` (bool): Allow or block changing partition count.
- `routerboard` (bool): Allow or block `/system/routerboard/settings` (except auto-upgrade) and SwOS/RouterOS transition on dual-boot devices.
- `activation-timeout` (time): How long to wait for the physical confirmation (button press or power cycle) before the update is canceled. Also sets the length of the `attempt-count` reset window when an update is refused after three unsuccessful attempts. Range: 00:00:10 to 1d00:00:00. Default: 5m.

**Read-only arguments**

- `update` (string): Status of a pending update with the time left to confirm it; empty when no update is pending.
