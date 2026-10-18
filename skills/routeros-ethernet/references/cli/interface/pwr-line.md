# /interface/pwr-line

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/pwr-line

Syscap: pwrlink; Type: Directory

**Flags**

- `X`: disabled
- `R`: running
- `S`: slave

**Arguments**

- `name` (string)
- `mtu` (num)
- `l2mtu` (num)
- `mac-address` (macAddr)
- `orig-mac-address` (macAddr)
- `tx-flow-control` (enum: off | on | auto)
- `rx-flow-control` (enum: off | on | auto)
- `arp` (enum: disabled | enabled | proxy-arp | reply-only | local-proxy-arp)
- `arp-timeout` (alt { arp-timeout: enum (auto) , arp-timeout: time })
- `arp-accept` (bool)
- `loop-protect` (enum: default | off | on)
- `loop-protect-send-interval` (time)
- `loop-protect-disable-time` (time)

**Read-only arguments**

- `default-name` (string)
- `switch` (enum; syscap=switch)
- `loop-protect-status` (enum: off | on | disabled)
- `driver-rx-byte` (multi { counter: num })
- `driver-rx-packet` (multi { counter: num })
- `driver-tx-byte` (multi { counter: num })
- `driver-tx-packet` (multi { counter: num })
- `rx-bytes` (multi { counter: num })
- `rx-packet` (multi { counter: num })
- `rx-too-short` (multi { counter: num })
- `rx-64` (multi { counter: num })
- `rx-65-127` (multi { counter: num })
- `rx-128-255` (multi { counter: num })
- `rx-256-511` (multi { counter: num })
- `rx-512-1023` (multi { counter: num })
- `rx-1024-1518` (multi { counter: num })
- `rx-1519-max` (multi { counter: num })
- `rx-too-long` (multi { counter: num })
- `rx-broadcast` (multi { counter: num })
- `rx-pause` (multi { counter: num })
- `rx-multicast` (multi { counter: num })
- `rx-fcs-error` (multi { counter: num })
- `rx-align-error` (multi { counter: num })
- `rx-fragment` (multi { counter: num })
- `rx-overflow` (multi { counter: num })
- `rx-control` (multi { counter: num })
- `rx-unknown-op` (multi { counter: num })
- `rx-length-error` (multi { counter: num })
- `rx-code-error` (multi { counter: num })
- `rx-carrier-error` (multi { counter: num })
- `rx-jabber` (multi { counter: num })
- `rx-drop` (multi { counter: num })
- `rx-ip-header-checksum-error` (multi { counter: num })
- `rx-tcp-checksum-error` (multi { counter: num })
- `rx-udp-checksum-error` (multi { counter: num })
- `tx-bytes` (multi { counter: num })
- `tx-packet` (multi { counter: num })
- `tx-too-short` (multi { counter: num })
- `tx-64` (multi { counter: num })
- `tx-65-127` (multi { counter: num })
- `tx-128-255` (multi { counter: num })
- `tx-256-511` (multi { counter: num })
- `tx-512-1023` (multi { counter: num })
- `tx-1024-1518` (multi { counter: num })
- `tx-1519-max` (multi { counter: num })
- `tx-too-long` (multi { counter: num })
- `tx-broadcast` (multi { counter: num })
- `tx-pause` (multi { counter: num })
- `tx-multicast` (multi { counter: num })
- `tx-underrun` (multi { counter: num })
- `tx-collision` (multi { counter: num })
- `tx-excessive-collision` (multi { counter: num })
- `tx-multiple-collision` (multi { counter: num })
- `tx-single-collision` (multi { counter: num })
- `tx-excessive-deferred` (multi { counter: num })
- `tx-deferred` (multi { counter: num })
- `tx-late-collision` (multi { counter: num })
- `tx-total-collision` (multi { counter: num })
- `tx-pause-honored` (multi { counter: num })
- `tx-drop` (multi { counter: num })
- `tx-jabber` (multi { counter: num })
- `tx-fcs-error` (multi { counter: num })
- `tx-control` (multi { counter: num })
- `tx-fragment` (multi { counter: num })
- `tx-carrier-sense-error` (multi { counter: num })
- `tx-rx-64` (multi { counter: num })
- `tx-rx-65-127` (multi { counter: num })
- `tx-rx-128-255` (multi { counter: num })
- `tx-rx-256-511` (multi { counter: num })
- `tx-rx-512-1023` (multi { counter: num })
- `tx-rx-1024-1518` (multi { counter: num })
- `tx-rx-1519-max` (multi { counter: num })
- `tx-queue-custom0-drop-packet` (multi { counter: num })
- `tx-queue-custom0-drop-byte` (multi { counter: num })
- `tx-queue-custom1-drop-packet` (multi { counter: num })
- `tx-queue-custom1-drop-byte` (multi { counter: num })
- `policy-drop-packet` (multi { counter: num })
- `custom-drop-packet` (multi { counter: num })
- `current-learned` (multi { counter: num })
- `not-learned` (multi { counter: num })
- `rx-unicast` (multi { counter: num })
- `tx-unicast` (multi { counter: num })
- `rx-error-events` (multi { counter: num })
- `tx-rx-1024-max` (multi { counter: num })
- `rx-1024-max` (multi { counter: num })
- `tx-1024-max` (multi { counter: num })
- `rs-fec-codewords` (multi { counter: num })
- `rs-fec-corrected` (multi { counter: num })
- `rs-fec-uncorrected` (multi { counter: num })
- `rs-fec-symbol-error` (multi { counter: num })
- `fc-fec-rx-block` (multi { counter: num })
- `fc-fec-block-corrected` (multi { counter: num })
- `fc-fec-block-uncorrected` (multi { counter: num })
- `tx-queue0-packet` (multi { counter: num })
- `tx-queue0-byte` (multi { counter: num })
- `tx-queue1-packet` (multi { counter: num })
- `tx-queue1-byte` (multi { counter: num })
- `tx-queue2-packet` (multi { counter: num })
- `tx-queue2-byte` (multi { counter: num })
- `tx-queue3-packet` (multi { counter: num })
- `tx-queue3-byte` (multi { counter: num })
- `tx-queue4-packet` (multi { counter: num })
- `tx-queue4-byte` (multi { counter: num })
- `tx-queue5-packet` (multi { counter: num })
- `tx-queue5-byte` (multi { counter: num })
- `tx-queue6-packet` (multi { counter: num })
- `tx-queue6-byte` (multi { counter: num })
- `tx-queue7-packet` (multi { counter: num })
- `tx-queue7-byte` (multi { counter: num })
- `tx-drop-packet` (multi { counter: num })
- `tx-drop-byte` (multi { counter: num })
- `tx-drop-queue0-packet` (multi { counter: num })
- `tx-drop-queue0-byte` (multi { counter: num })
- `tx-drop-queue1-packet` (multi { counter: num })
- `tx-drop-queue1-byte` (multi { counter: num })
- `tx-drop-queue2-packet` (multi { counter: num })
- `tx-drop-queue2-byte` (multi { counter: num })
- `tx-drop-queue3-packet` (multi { counter: num })
- `tx-drop-queue3-byte` (multi { counter: num })
- `tx-drop-queue4-packet` (multi { counter: num })
- `tx-drop-queue4-byte` (multi { counter: num })
- `tx-drop-queue5-packet` (multi { counter: num })
- `tx-drop-queue5-byte` (multi { counter: num })
- `tx-drop-queue6-packet` (multi { counter: num })
- `tx-drop-queue6-byte` (multi { counter: num })
- `tx-drop-queue7-packet` (multi { counter: num })
- `tx-drop-queue7-byte` (multi { counter: num })

## Commands

### /interface/pwr-line/blink

Syscap: pwrlink; Type: Command

### /interface/pwr-line/configure

Syscap: pwrlink; Type: Command

**Arguments**

- `network-key` (string)
- `network-password` (string)
- `plc-cco-selection-mode` (enum: auto | never | always)

### /interface/pwr-line/join

Syscap: pwrlink; Type: Command

### /interface/pwr-line/leave

Syscap: pwrlink; Type: Command

### /interface/pwr-line/monitor

Syscap: pwrlink; Type: Command

**Read-only arguments**

- `name` (string)
- `connection-to-plc` (enum: ok | no-link)
- `tx-flow-control` (bool)
- `rx-flow-control` (bool)
- `phy-regs` (multi { array-id, method: string })
- `plc-actual-network-key` (string)
- `plc-hw-platform` (string)
- `plc-sw-platform` (string)
- `plc-fw-version` (string)
- `plc-line-freq` (enum: unknown | 50Hz | 60Hz)
- `plc-zero-crossing` (enum: not-yet-detected | detected | missing)
- `plc-role` (enum: station | proxy-coordinator | central-coordinator)
- `plc-station-count` (num)
- `plc-mac` (macAddr)
- `plc-cco-mac` (macAddr)
- `plc-station-info` (string)

### /interface/pwr-line/reset-counters

Syscap: pwrlink; Type: Command

### /interface/pwr-line/reset-mac-address

Syscap: pwrlink; Type: Command

### /interface/pwr-line/upgrade-firmware

Syscap: pwrlink; Type: Command

**Arguments**

- `firmware-file` (file)
- `pib-file` (file)
