# /system/ntp/monitor-peers

> Source: https://manual.mikrotik.com/docs/cli-reference/system/ntp/monitor-peers

Type: Command

Continuously prints the client's view of its time sources, updating in place. Includes the local reference clock (127.127.1.0) when `use-local-clock` is enabled. See the [NTP](../../../guides/system-information-and-utilities/ntp.md) guide.

**Read-only arguments**

- `type` (string): Association type, for example `ucast-client` for a unicast server.
- `address` (address (flags=46)): Peer address from the server list, or 127.127.1.0 for the local reference clock.
- `refid` (string): Reference ID: the time source of the peer (typically the address of the peer's own upstream source). Empty while the peer is unsynchronized.
- `stratum` (num): Stratum announced by the peer. 16 means unsynchronized.
- `hpoll` (num): Current poll interval to this peer, as the power of 2 in seconds (6 = 64 s).
- `ppoll` (num): Poll interval the peer asks for, as the power of 2 in seconds.
- `root-delay` (num): Total round-trip delay from the peer to the root (stratum 1) time source.
- `root-disp` (num): Maximum error of the peer relative to the root time source.
- `offset` (num): Estimated clock offset of the peer relative to the local clock.
- `delay` (num): Round-trip delay to the peer.
- `disp` (num): Dispersion of the peer: the accumulated measurement error of its time.
- `jitter` (num): Variation of the offset between consecutive samples.
