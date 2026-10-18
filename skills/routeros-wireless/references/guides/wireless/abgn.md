# 802.11 a/b/g/n

> Source: https://manual.mikrotik.com/docs/wireless/abgn
>
> MikroTik 802.11 a/b/g/n devices use the legacy /interface/wireless menu provided by the wireless package. This section covers the wireless interface, MikroTik-proprietary protocols (Nstreme, Nv2), HWMP+ mesh,...

This section covers MikroTik **802.11 a/b/g/n** devices (and any 802.11ac device running the `wireless` package), configured through the **`/interface/wireless`** menu (the **`wireless`** driver package) — the only option on MIPS-based devices.

This menu is also where the MikroTik-specific, throughput-oriented features live — **Nstreme** and **Nv2** (TDMA), **WDS**, and **HWMP+ mesh** — as well as the original **[CAPsMAN](abgn/capsman/ap-controller-capsman.md)** (`/caps-man`) controller.

> **Info**
>
> Some 802.11ac devices can instead run the new `/interface/wifi` menu via the `wifi-qcom-ac` package — see [Wi-Fi 5 (802.11ac)](https://manual.mikrotik.com/docs/wireless/wifi-ac/index) to choose. WPA3 and fast roaming are only available through the new menu.
