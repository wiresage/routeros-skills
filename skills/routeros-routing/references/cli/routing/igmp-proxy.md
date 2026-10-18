# /routing/igmp-proxy

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/igmp-proxy

Type: Settings Directory

**Arguments**

- `robustness` (num): The robustness value of the IGMP proxy, used as the retransmission count for queries and the tolerance for lost packets. Interfaces without their own robustness setting inherit this value.
- `query-interval` (time): How often to send out IGMP Query messages over downstream interfaces.
- `query-response-interval` (time): How long to wait for responses to an IGMP Query message.
- `last-member-query-interval` (time): The timeout for group-specific queries sent to verify that no group members remain after a Leave message.
