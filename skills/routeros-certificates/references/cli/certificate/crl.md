# /certificate/crl

> Source: https://manual.mikrotik.com/docs/cli-reference/certificate/crl

Type: Directory

**Flags**

- `E`: expired
- `D`: dynamic
- `I`: invalid

**Arguments**

- `url` (string; mandatory)

**Read-only arguments**

- `cert` (enum: none)
- `trust-store` (alt { all: enum (all) , component: ubit (ipsec, wpa-eap, capsman, fetch, sstp, ovpn, mqtt, email, netwatch, radius, container, userman, lora, wiliot, openflow, tr069, dot1x, dns, www, api, reverse-proxy, logging) })
- `num` (num)
- `revoked` (num)
- `next-update` (date)
- `last-update` (date)
- `akid` (string)
- `fingerprint` (string)
- `signature` (string)

## Commands

### /certificate/crl/download

Type: Command

### /certificate/crl/flush

Type: Command
