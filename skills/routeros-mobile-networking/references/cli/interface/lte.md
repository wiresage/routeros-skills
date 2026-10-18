# /interface/lte

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/lte

Conditions: !smips; Type: Directory

**Flags**

- `X`: disabled
- `R`: running
- `I`: inactive

**Arguments**

- `name` (string)
- `mtu` (num)
- `master` (iface_enum; mandatory)
- `pin` (string)
- `apn-profiles` (enum; deprecated)
- `apn-profile` (enum; mandatory)
- `modem-init` (string): string to send upon modem initialization
- `operator` (string): operator locking, use numeric value: mccmnc
- `allow-roaming` (bool)
- `sms-read` (bool): This setting is ignored if any interface is enabled in /tool/sms
- `sms-protocol` (enum: mbim | at | qmi | auto)
- `network-mode` (multi { array-id, network: enum })
- `band` (multi { array-id, band: enum }): LTE band
- `nr-band` (multi { array-id, nr-band: enum }): NR band

**Read-only arguments**

- `default-name` (string)
- `advertised-mtu` (num)

## Commands

### /interface/lte/at-chat

Conditions: !smips; Type: Command

**Arguments**

- `input` (string): sends command to modem and waits for any output before returning
- `wait` (alt { wait: enum (no | yes) }): always wait 3s

**Read-only arguments**

- `output` (string)

### /interface/lte/cell-monitor

Conditions: !smips; Type: Command

**Arguments**

- `max-age` (time)

**Read-only arguments**

- `phy-cellid` (num)
- `band` (string)
- `psc` (num)
- `earfcn` (string)
- `rsrp` (num)
- `rsrq` (num)
- `rssi` (num)
- `sinr` (num)
- `rscp` (num)
- `age` (time)

### /interface/lte/firmware-upgrade

Conditions: !smips; Type: Command

**Arguments**

- `upgrade` (bool): perform the upgrade or just check
- `firmware-file` (file): path or url for the upgrade image
- `update-channel` (enum: stable | testing): firmware update channel

**Read-only arguments**

- `installed` (string)
- `latest` (string)
- `note` (string)
- `status` (string)

### /interface/lte/monitor

Conditions: !smips; Type: Command

**Read-only arguments**

- `status` (string)
- `pin-status` (string)
- `registration-status` (string)
- `functionality` (enum: minimum | full | tx rf circuit disabled | rx rf circuit disabled | tx and rx rf circuit disabled | tx and rx rf circuit disabled)
- `manufacturer` (string)
- `model` (string)
- `revision` (string)
- `current-operator` (string)
- `roaming` (bool)
- `psc` (num)
- `lac` (num)
- `current-cellid` (num)
- `enb-id` (num)
- `sector-id` (num)
- `phy-cellid` (num)
- `data-class` (string)
- `session-uptime` (time)
- `imei` (string)
- `imsi` (string)
- `iccid` (string)
- `subscriber-number` (string)
- `earfcn` (string)
- `primary-band` (string)
- `ca-band` (multi { array-id, ca: string })
- `ul-ca-band` (multi { array-id, ca: string })
- `frame-error-rate` (string)
- `dl-modulation` (string)
- `dl-mimo` (num)
- `cqi` (num)
- `ri` (num)
- `mcs` (num)
- `ecio` (num)
- `rscp` (num)
- `rssi` (num)
- `rsrp` (num)
- `rsrq` (num)
- `sinr` (num)
- `nr-dl-modulation` (string)
- `nr-rsrp` (num)
- `nr-rsrq` (num)
- `nr-sinr` (num)

### /interface/lte/run-modem-update

Conditions: !smips; Type: Command

**Read-only arguments**

- `status` (string)

### /interface/lte/scan

Conditions: !smips; Type: Command

**Flags**

- `C`: current
- `A`: available
- `F`: forbidden

**Read-only arguments**

- `operator` (string)
- `mcc-mnc` (string)
- `access-technology` (string)
- `rssi` (num)
- `rsrp` (num)
- `rsrq` (num)

### /interface/lte/show-capabilities

Conditions: !smips; Type: Command

**Read-only arguments**

- `modem-bus-location` (string)
- `cell-scan` (bool)
- `network-scan` (bool)
- `roaming-barring` (bool)
- `apn-address-family` (string)
- `max-apn-count` (num)
- `rat-modes` (string)
- `band-selection` (bool)
- `lte-bands` (string)
- `nr-bands` (string)
- `passthrough` (bool)
- `esim-detected` (bool)
- `firmware-upgrade` (bool)
- `lte-attach-config` (bool)
- `at-chat` (bool)
- `framed-route-apn` (string)
