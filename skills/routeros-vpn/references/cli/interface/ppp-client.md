# /interface/ppp-client

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ppp-client

Type: Directory

**Flags**

- `X`: disabled
- `R`: running

**Arguments**

- `name` (string)
- `max-mtu` (num)
- `max-mru` (num)
- `mrru` (num)
- `port` (enum)
- `data-channel` (num)
- `info-channel` (num)
- `network-mode` (enum: lte-m | nb-iot | auto)
- `apn` (string)
- `pin` (string)
- `user` (string)
- `password` (string)
- `remote-address` (ipAddr)
- `profile` (enum)
- `phone` (string)
- `dial-command` (string)
- `modem-init` (string)
- `null-modem` (bool)
- `dial-on-demand` (bool)
- `add-default-route` (bool)
- `default-route-distance` (num)
- `use-peer-dns` (bool)
- `keepalive-timeout` (num)
- `allow` (ubit (pap, chap, mschap1, mschap2))

## Commands

### /interface/ppp-client/at-chat

Type: Command

**Arguments**

- `input` (string): sends command to modem and waits for any output before returning

**Read-only arguments**

- `output` (string)

### /interface/ppp-client/firmware-upgrade

Type: Command

**Arguments**

- `upgrade` (bool): perform the upgrade or just check
- `firmware-file` (file): path or url for the upgrade image
- `update-channel` (enum: stable | testing): firmware update channel

**Read-only arguments**

- `installed` (string)
- `latest` (string)
- `status` (string)
- `note` (string)

### /interface/ppp-client/info

Type: Command

**Arguments**

- `user-command` (string)

**Read-only arguments**

- `modem-status` (string)
- `pin-status` (string)
- `functionality` (string)
- `manufacturer` (string)
- `model` (string)
- `revision` (string)
- `serial-number` (string)
- `current-operator` (string)
- `phy-cellid` (num)
- `current-cellid` (num)
- `access-technology` (string)
- `imsi` (string)
- `iccid` (string)
- `signal-strength` (string)
- `frame-error-rate` (string)
- `user-command` (string)
- `rsrp` (num)
- `rsrq` (num)
- `sinr` (num)
- `earfcn` (num)

### /interface/ppp-client/monitor

Type: Command

**Read-only arguments**

- `status` (string)
- `uptime` (time)
- `encoding` (string)
- `connect-speed` (num)
- `mtu` (num)
- `mru` (num)
- `local-address` (ipAddr)
- `remote-address` (ipAddr)
- `local-ipv6-address` (ip6Addr)
- `remote-ipv6-address` (ip6Addr)

### /interface/ppp-client/scan

Type: Command

**Flags**

- `C`: current
- `A`: available
- `F`: forbidden

**Read-only arguments**

- `operator` (string)
- `mcc-mnc` (num)
- `access-technology` (string)
- `signal-strength` (num)
