# /caps-man/rates

> Source: https://manual.mikrotik.com/docs/cli-reference/caps-man/rates

Package: wireless-rep; Type: Directory

**Arguments**

- `name` (string; mandatory)
- `basic` (ubit (1Mbps, 2Mbps, 5.5Mbps, 11Mbps, 6Mbps, 9Mbps, 12Mbps, 18Mbps, 24Mbps, 36Mbps, 48Mbps, 54Mbps); unset)
- `supported` (ubit (1Mbps, 2Mbps, 5.5Mbps, 11Mbps, 6Mbps, 9Mbps, 12Mbps, 18Mbps, 24Mbps, 36Mbps, 48Mbps, 54Mbps); unset)
- `ht-basic-mcs` (ubit (mcs-0, mcs-1, mcs-2, mcs-3, mcs-4, mcs-5, mcs-6, mcs-7, mcs-8, mcs-9, mcs-10, mcs-11, mcs-12, mcs-13, mcs-14, mcs-15, mcs-16, mcs-17, mcs-18, mcs-19, mcs-20, mcs-21, mcs-22, mcs-23); unset)
- `ht-supported-mcs` (ubit (mcs-0, mcs-1, mcs-2, mcs-3, mcs-4, mcs-5, mcs-6, mcs-7, mcs-8, mcs-9, mcs-10, mcs-11, mcs-12, mcs-13, mcs-14, mcs-15, mcs-16, mcs-17, mcs-18, mcs-19, mcs-20, mcs-21, mcs-22, mcs-23); unset)
- `vht-basic-mcs` (multi { array-id, mcs-set: enum (none | mcs0-7 | mcs0-8 | mcs0-9) }; unset)
- `vht-supported-mcs` (multi { array-id, mcs-set: enum (none | mcs0-7 | mcs0-8 | mcs0-9) }; unset)
