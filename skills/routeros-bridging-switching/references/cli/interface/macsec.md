# /interface/macsec

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/macsec

Conditions: !smips; Type: Directory

**Flags**

- `I`: inactive
- `X`: disabled
- `R`: running
- `H`: hw-offloaded

**Arguments**

- `name` (string)
- `mtu` (num)
- `interface` (iface_enum; mandatory)
- `cak` (string)
- `ckn` (string)
- `profile` (enum)

**Read-only arguments**

- `status` (string)
- `tx-untagged` (num)
- `rx-untagged` (num)
- `tx-too-long` (num)
- `rx-no-tag` (num)
- `rx-bad-tag` (num)
- `rx-unknown-sci` (num)
- `rx-no-sci` (num)
- `rx-overrun` (num)
- `tx-sc-protected-byte` (multi { counter: num })
- `tx-sc-protected-packet` (multi { counter: num })
- `tx-sc-encrypted-byte` (multi { counter: num })
- `tx-sc-encrypted-packet` (multi { counter: num })
- `rx-sc-validated-byte` (multi { counter: num })
- `rx-sc-decrypted-byte` (multi { counter: num })
- `rx-sc-unchecked` (multi { counter: num })
- `rx-sc-delayed` (multi { counter: num })
- `rx-sc-ok` (multi { counter: num })
- `rx-sc-invalid` (multi { counter: num })
- `rx-sc-late` (multi { counter: num })
- `rx-sc-not-valid` (multi { counter: num })
- `rx-sc-not-using-sa` (multi { counter: num })
- `rx-sc-unused-sa` (multi { counter: num })
- `rx-sa-ok` (multi { counter: num })
- `rx-sa-invalid` (multi { counter: num })
- `rx-sa-not-valid` (multi { counter: num })
- `rx-sa-not-using-sa` (multi { counter: num })
- `rx-sa-unused-sa` (multi { counter: num })
- `tx-sa-protected` (multi { counter: num })
- `tx-sa-encrypted` (multi { counter: num })

## Commands

### /interface/macsec/monitor

Conditions: !smips; Type: Command

**Read-only arguments**

- `key-server` (bool)
- `cipher-suite` (enum: aes-gcm-128 | aes-gcm-xpn-128)
