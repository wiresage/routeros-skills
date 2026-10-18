# /caps-man/radio

> Source: https://manual.mikrotik.com/docs/cli-reference/caps-man/radio

Package: wireless-rep; Type: Directory

**Flags**

- `L`: local
- `P`: provisioned

**Read-only arguments**

- `radio-mac` (macAddr)
- `remote-cap-name` (string)
- `remote-cap-identity` (string)
- `interface` (iface_enum)

## Commands

### /caps-man/radio/hw-info

Package: wireless-rep; Type: Command

**Read-only arguments**

- `ranges` (multi { array-id, range: string })
- `tx-chains` (ubit (0, 1, 2, 3))
- `rx-chains` (ubit (0, 1, 2, 3))
- `antenna-gain` (num)
- `locked-countries` (multi { array-id, country: enum })

### /caps-man/radio/provision

Package: wireless-rep; Type: Command
