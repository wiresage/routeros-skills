# /ip/upnp

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/upnp

Type: Settings Directory

Universal Plug and Play (UPnP) service settings. The service answers SSDP discovery on UDP port 1900 and control connections on TCP port 2828 of each [internal interface](upnp/interfaces.md). Any change in this menu restarts the service: all dynamic port mappings are removed and clients have to request them again. Configuration examples are on the [UPnP guide page](../../guides/firewall-and-quality-of-service/upnp.md).

**Arguments**

- `enabled` (bool): Enable the UPnP service. Default: no.
- `allow-disable-external-interface` (bool): Allow UPnP clients on the internal interfaces to disable the router's external interface with the `ForceTermination` action, without any authentication. The UPnP standard requires this action to work; set to `no` so local clients cannot take the Internet connection down. Disabling the external interface this way also removes its dynamic port mappings. Default: no.
- `show-dummy-rule` (bool): Report an inactive placeholder port mapping (port 0, client 0.0.0.0, description "Dummy inactive rule for windows to work") as the first entry when a client enumerates port mappings. A workaround for client applications that misbehave when no port mappings exist. The dummy entry never appears in `/ip/firewall/nat`. Default: yes.
