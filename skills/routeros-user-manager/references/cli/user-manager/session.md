# /user-manager/session

> Source: https://manual.mikrotik.com/docs/cli-reference/user-manager/session

Package: userman-5; Type: Directory

**Flags**

- `A`: active

**Read-only arguments**

- `user` (enum)
- `acct-session-id` (string)
- `acct-multi-session-id` (string)
- `nas-port-type` (enum: async | sync | isdn-sync | isdn-sync-v120 | isdn-sync-v110 | virtual | piafs | hdlc | x25 | x75 | g3-fax | sdsl | adsl-cap | adsl-dmt | idsl | ethernet | dsl | cable | wireless | wireless-802.11)
- `nas-port-id` (string)
- `nas-ip-address` (alt { ip-address: ipAddr , ipv6-address: ip6Addr })
- `nas-identifier` (string)
- `calling-station-id` (string)
- `user-address` (ipAddr)
- `status` (ubit (start, stop, interim, close-acked, expired))
- `started` (date)
- `ended` (date)
- `terminate-cause` (enum: user-request | lost-carrier | lost-service | idle-timeout | session-timeout | admin-reset | admin-reboot | port-error | nas-error | nas-request | nas-reboot | port-unneeded | port-preempted | port-suspended | service-unavailable | callback | user-error | host-request | supplicant-restart | reauthentication-failure | port-reinitialized | port-administratively-disabled | um-user-deleted | um-user-disabled | um-admin-request | um-nas-rebooted | um-simultaneous-sessions | um-limits-reached | um-limits-changed | um-unknown)
- `uptime` (time)
- `download` (num)
- `upload` (num)
- `last-accounting-packet` (date)

## Commands

### /user-manager/session/close-session

Package: userman-5; Type: Command
