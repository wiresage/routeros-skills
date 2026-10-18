# /system/leds

> Source: https://manual.mikrotik.com/docs/cli-reference/system/leds

Type: Directory

**Flags**

- `X`: disabled
- `*`: default

**Arguments**

- `type` (enum: interface-status | interface-receive | interface-transmit | interface-activity | wireless-signal-strength | wireless-status | modem-signal | modem-technology | flash-access | interface-speed | interface-speed-1G | interface-speed-25G | interface-speed-2.5G | interface-speed-100G | poe-out | ap-cap | on | off | fan-fault | poe-fault | gps-valid | align-left | align-right | align-up | align-down; mandatory)
- `leds` (object { led: enum }; mandatory)
- `interface` (object { iface: iface_enum })
- `modem-signal-threshold` (num): RSSI threshold
- `color` (alt { color-name: enum (none | red | orange | yellow | green-yellow | green | green-cyan | cyan | blue-cyan | blue | blue-magenta | magenta | red-magenta) { none:0, red:0xff0000, orange:0xff7f00, yellow:0xffff00, green-yellow:0x7fff00, green:0x00ff00, green-cyan:0x00ff7f, cyan:0x00ffff, blue-cyan:0x007fff, blue:0x0000ff, blue-magenta:0x7f00ff, magenta:0xff00ff, red-magenta:0xff007f } , color-number: num [0 .. 0xffffff] })
