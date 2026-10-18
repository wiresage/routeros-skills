# /ip/hotspot/profile

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/hotspot/profile

Type: Directory

**Flags**

- `*`: default

**Arguments**

- `name` (string)
- `hotspot-address` (ipAddr)
- `dns-name` (string)
- `html-directory` (file)
- `html-directory-override` (file)
- `install-hotspot-queue` (bool)
- `rate-limit` (string)
- `http-proxy` (composite { address: ipAddr , port: num [0 .. 65535] })
- `smtp-server` (ipAddr)
- `login-by` (ubit (mac, cookie, http-chap, https, http-pap, trial, mac-cookie))
- `mac-auth-mode` (enum: mac-as-username | mac-as-username-and-password)
- `mac-auth-password` (string)
- `http-cookie-lifetime` (time)
- `ssl-certificate` (enum: none)
- `split-user-domain` (bool)
- `trial-uptime-limit` (time)
- `trial-uptime-reset` (time)
- `trial-user-profile` (enum)
- `use-radius` (bool)
- `radius-accounting` (bool)
- `radius-interim-update` (alt { symbolic-names: enum (received) , time-interval: time })
- `nas-port-type` (enum: ethernet | cable | wireless-802.11)
- `radius-default-domain` (string)
- `radius-location-id` (string)
- `radius-location-name` (string)
- `radius-mac-format` (enum (XX:XX:XX:XX:XX:XX | XXXX:XXXX:XXXX | XXXXXX:XXXXXX | XX-XX-XX-XX-XX-XX | XXXXXX-XXXXXX | XXXXXXXXXXXX | XX XX XX XX XX XX) { XX:XX:XX:XX:XX:XX:0, XXXX:XXXX:XXXX:1, XXXXXX:XXXXXX:2, XX-XX-XX-XX-XX-XX:3, XXXXXX-XXXXXX:4, XXXXXXXXXXXX:5, XX XX XX XX XX XX:6 })
