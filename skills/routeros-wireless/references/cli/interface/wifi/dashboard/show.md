# /interface/wifi/dashboard/show

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/wifi/dashboard/show

Type: Command

**Arguments**

- `interface` (multi { array-id, interface: iface_enum }; unset)

**Read-only arguments**

- `ifaces` (num)
- `aps-total` (num)
- `aps-run` (num)
- `slaveaps-total` (num)
- `aps-2g` (num)
- `aps-5g` (num)
- `aps-6g` (num)
- `aps-be` (num)
- `aps-ax` (num)
- `aps-ac` (num)
- `aps-n` (num)
- `aps-ofdm` (num)
- `stas-total` (num)
- `stas-2ghz` (num)
- `stas-5ghz` (num)
- `stas-6ghz` (num)
- `stas-open` (num)
- `stas-wpa` (num)
- `stas-wpa2` (num)
- `stas-wpa3` (num)
- `stas-eap` (num)
- `stas-ft` (num)
- `stas-be` (num)
- `stas-ax` (num)
- `stas-ac` (num)
- `stas-n` (num)
- `stas-ofdm` (num)
- `bw-total-down` (num)
- `bw-total-up` (num)
- `ap-freqs` (multi { array-id, array-id, array-id, range: super { start: num , [end] -num , [value] :num } })
- `sta-freqs` (multi { array-id, array-id, array-id, range: super { start: num , [end] -num , [value] :num } })
