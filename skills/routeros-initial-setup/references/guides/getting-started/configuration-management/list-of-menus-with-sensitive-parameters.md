# List of menus with sensitive parameters

> Source: https://manual.mikrotik.com/docs/getting-started/configuration-management/list-of-menus-with-sensitive-parameters
>
> This page lists MikroTik RouterOS menus where sensitive parameters such as passwords, keys, and secrets are configured, with links to detailed documentation for each.

Below you can find a list of menus where sensitive (shown only when [show-sensitive parameter](https://manual.mikrotik.com/docs/getting-started/configuration-management/index#configuration-export) is used or alternatively hidden when "Hide password" is enabled in WinBox settings) parameters can be configured. For more detailed information, please refer to the corresponding menu documentation pages.

| Menu | Parameter names | Page link |
| :-- | :-- | :-- |
| `/container` | password | [Container#Containerconfiguration](https://manual.mikrotik.com/docs/containers/index) |
| `/ip/hotspot` | mac-auth-password, password, otp-secret | [HotSpot - Captive portal#HotSpotUsers](https://manual.mikrotik.com/docs/authentication-authorization-accounting/hotspot-captive-portal/index) |
| `/iot` | password, key | password - [MQTT#Brokers](https://manual.mikrotik.com/docs/internet-of-things/mqtt/index)  key - [Lora#Servers](https://manual.mikrotik.com/docs/internet-of-things/lora/general-properties#servers)|
| `/interface/gre`  `/interface/gre6` | ipsec-secret | [GRE#Properties](https://manual.mikrotik.com/docs/virtual-private-networks/gre) |
| `/interface/ipip`  `/interface/ipipv6` | ipsec-secret | [IPIP#Properties](https://manual.mikrotik.com/docs/virtual-private-networks/ipip) |
| `/interface/eoip`  `/interface/eoipv6` | ipsec-secret | [EoIP#PropertyDescription](https://manual.mikrotik.com/docs/virtual-private-networks/eoip) |
| `/interface/6to4` | ipsec-secret | [6to4#6to4-PropertyDescription](https://manual.mikrotik.com/docs/virtual-private-networks/6to4) |
| `/interface/ppp-client` | password, pin | Work in Progress [PPP](https://manual.mikrotik.com/docs/mobile-networking/ppp) |
| `/interface/sstp-client` | password | [SSTP#Properties](https://manual.mikrotik.com/docs/virtual-private-networks/sstp) |
| `/interface/l2tp-server`  `/interface/l2tp-client`  `/interface/l2tp-ether` | ipsec-secret, password | ipsec-secret, password - [L2TP#L2TPClient](https://manual.mikrotik.com/docs/virtual-private-networks/l2tp/index#l2tp-client)  ipsec-secret - [L2TP#L2TPServer](https://manual.mikrotik.com/docs/virtual-private-networks/l2tp/index#l2tp-server)  ipsec-secret - [L2TP#L2TPEther](https://manual.mikrotik.com/docs/virtual-private-networks/l2tp/index#l2tp-ether)|
| `/interface/ovpn-client` | password | [OpenVPN#OVPNClient](https://manual.mikrotik.com/docs/virtual-private-networks/openvpn) |
| `/interface/pptp-client` | password | [PPTP#PPTPClient](https://manual.mikrotik.com/docs/virtual-private-networks/pptp) |
| `/interface/pppoe-client` | password | [PPPoE#PPPoEClient](https://manual.mikrotik.com/docs/virtual-private-networks/pppoe/index) |
| `/ppp/secret` | password | [PPP AAA#UserDatabase](https://manual.mikrotik.com/docs/authentication-authorization-accounting/ppp-aaa) |
| `/ppp/l2tp-secret` | secret | Work in Progress |
| `/ip/ssh/export-host-key`  `/ip/ssh/import-host-key` | passphrase | [SSH](https://manual.mikrotik.com/docs/management-tools/ssh#server-host-key) |
| `/ip/ipsec` | auth-key, enc-key, ppk-secret, secret, password, passphrase, key | auth-key, enc-key - [IPsec InstalledSA](https://manual.mikrotik.com/docs/cli-reference/ip/ipsec/installed-sa)  secret, password - [IPsec Identity](https://manual.mikrotik.com/docs/cli-reference/ip/ipsec/identity)  ppk-secret - Work in Progress [IPsec Peer](https://manual.mikrotik.com/docs/cli-reference/ip/ipsec/peer)  key, passphrase - Work in Progress IPsec Keys|
| `/system/ssh-exec` | password | [SSH](https://manual.mikrotik.com/docs/management-tools/ssh#run-remote-commands-from-scripts) |
| `/user` | password, passphrase | [User](https://manual.mikrotik.com/docs/authentication-authorization-accounting/user) |
| `/disk` | nvme-tcp-server-password, nvme-tcp-password, smb-server-password, smb-password, self-encryption-password, encryption-key, sshfs-password | nvme-tcp-server-password, nvme-tcp-password - [NVMe over TCP](https://manual.mikrotik.com/docs/storage/nvme-over-tcp)  sshfs-password - Work in Progress  smb-server-password, smb-password - [SMB](https://manual.mikrotik.com/docs/storage/smb)  self-encryption-password, encryption-key - [Self-Encrypting Drives](https://manual.mikrotik.com/docs/storage/self-encrypting-drives)|
| `/interface/vrrp` | password | [VRRP#Parameters](https://manual.mikrotik.com/docs/high-availability-solutions/vrrp) |
| `/interface/dot1x` | password | [Dot1X#Client](https://manual.mikrotik.com/docs/authentication-authorization-accounting/dot1x) |
| `/interface/macsec` | cak | [MACsec#PropertyReference](https://manual.mikrotik.com/docs/bridging-and-switching/macsec) |
| `/interface/wireguard` | private-key, preshared-key, \**show-client-config* | [WireGuard](https://manual.mikrotik.com/docs/virtual-private-networks/wireguard) |
| `/interface/lte` | pin, password | [LTE/5G#LTEClient](https://manual.mikrotik.com/docs/mobile-networking/lte-5g#lte-client) |
| `/ip/socks/users` | password | [SOCKS](https://manual.mikrotik.com/docs/network-management/socks/index) |
| `/ip/cloud` | vpn-private-key, vpn-peer-private-key, private-key | [Back To Home](https://manual.mikrotik.com/docs/network-management/cloud/back-to-home) |
| `/ip/smb` | password | [SMB#Usersetup](https://manual.mikrotik.com/docs/storage/smb) |
| `/password` | old-password, new-password, confirm-new-password | Password change command; no dedicated documentation page available. |
| `/radius` | secret | [RADIUS#RADIUSClient](https://manual.mikrotik.com/docs/authentication-authorization-accounting/radius) |
| `/routing` | password, tcp-md5-key, auth-key, key | password,key - [/routing/rip](https://manual.mikrotik.com/docs/cli-reference/routing/rip/instance)  tcp-md5-key - [/routing/bgp/connection](https://manual.mikrotik.com/docs/cli-reference/routing/bgp/connection)  auth-key - [/routing/ospf](https://manual.mikrotik.com/docs/cli-reference/routing/ospf/interface-template)|
| `/snmp/community` | authentication-password, encryption-password | [SNMP#CommunityProperties](https://manual.mikrotik.com/docs/diagnostics-monitoring-and-troubleshooting/snmp) |
| `/system/backup` | password | [Backup](backup.md) |
| `/system/ntp/key` | key-val | Work in Progress [NTP](https://manual.mikrotik.com/docs/system-information-and-utilities/ntp) |
| `/system/swos/password` | new-password, confirm-new-password | SwOS password change command; no dedicated documentation page available. |
| `/system/package/local-update` | password | [Packages#LocalUpdate](https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/packages) |
| `/system/license` | password | [RouterOS license keys#CHRLicenseLevels](https://manual.mikrotik.com/docs/getting-started/routeros-licensing/chr/chr-licensing#chr-license-levels) |
| `/tool/romon` | secrets | [RoMON#Configuration](https://manual.mikrotik.com/docs/management-tools/romon) |
| `/tool/sms` | sim-pin, secret | [SMS#Receiving](https://manual.mikrotik.com/docs/mobile-networking/sms) |
| `/tool/email` | password | [E-mail](https://manual.mikrotik.com/docs/system-information-and-utilities/e-mail) |
| `/tr069-client` | connection-request-password, password | [TR-069#ConfigurationSettings](https://manual.mikrotik.com/docs/management-tools/tr-069) |
| `/user-manager` | web-private-password, paypal-password, shared-secret, password, otp-secret | shared-secret - [User Manager#Routers](https://manual.mikrotik.com/docs/authentication-authorization-accounting/user-manager#routers)  paypal-password, web-private-password - [User Manager#Advanced](https://manual.mikrotik.com/docs/authentication-authorization-accounting/user-manager#advanced)  password, otp-secret - [User Manager#Users](https://manual.mikrotik.com/docs/authentication-authorization-accounting/user-manager#users)|
| `/interface/wifi` | passphrase, eap-password | [WiFi#SecurityProperties](https://manual.mikrotik.com/docs/wireless/wifi/index) |
| `/caps-man` | private-passphrase, passphrase | private-passphrase - [CAPsMAN#CAPsMANAccess-list](https://manual.mikrotik.com/docs/wireless/abgn/capsman/index#capsman-access-list)  passphrase - [CAPsMAN#CAPsMANconfiguration](https://manual.mikrotik.com/docs/wireless/abgn/capsman/index#capsman-configuration)|
| `/interface/wireless` | static-key-0, static-key-1, static-key-2, static-key-3, static-sta-private-key, management-protection-key, nv2-preshared-key, private-key, private-pre-shared-key, wpa-pre-shared-key, wpa2-pre-shared-key, mschapv2-password | static-key-0, static-key-1, static-key-2, static-key-3, static-sta-private-key - [Wireless Interface#WEPproperties](https://manual.mikrotik.com/docs/wireless/index)  management-protection-key, private-key, private-pre-shared-key - [Wireless Interface#Properties](https://manual.mikrotik.com/docs/wireless/index)  wpa-pre-shared-key, wpa2-pre-shared-key - [Wireless Interface#WPAproperties](https://manual.mikrotik.com/docs/wireless/index)  mschapv2-password - [Wireless Interface#WPAEAPproperties](https://manual.mikrotik.com/docs/wireless/index)  nv2-preshared-key - [Wireless Interface#Generalinterfaceproperties](https://manual.mikrotik.com/docs/wireless/index) |
| `/interface/w60g` | password | [W60G#Generalinterfaceproperties](https://manual.mikrotik.com/docs/wireless/w60g/index) |
| `/zerotier` | identity | [ZeroTier#Parameters](https://manual.mikrotik.com/docs/virtual-private-networks/zerotier) |
| `/certificate` | export-passphrase, passphrase, challenge-password, pin, key-passphrase, challenge-passphrase | pin - used for card-reinstall and card-verify commands, no dedicated documentation page available.  export-passphrase - [Certificates#ExportCertificate](https://manual.mikrotik.com/docs/authentication-authorization-accounting/certificates#export-certificate)  passphrase - [Certificates#ImportCertificate](https://manual.mikrotik.com/docs/authentication-authorization-accounting/certificates#import-certificate)  challenge-password, key-passphrase, challenge-passphrase - Work in progress |
