# /ip/hotspot/walled-garden/ip

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/hotspot/walled-garden/ip

Type: Directory

**Flags**

- `X`: disabled
- `I`: invalid

**Arguments**

- `server` (super { ! , server: enum })
- `src-address` (super { ! , range: ipRange })
- `dst-address` (super { ! , range: ipRange })
- `dst-host` (string)
- `protocol` (super { ! , protocol: enum () })
- `dst-port` (super { ! , min: num [0 .. 65535] , [max] -num [0 .. 65535] })
- `src-address-list` (super { ! , address-list: enum })
- `dst-address-list` (super { ! , address-list: enum })
- `action` (enum: accept | drop | reject)
