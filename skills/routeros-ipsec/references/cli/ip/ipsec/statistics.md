# /ip/ipsec/statistics

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/ipsec/statistics

Type: Settings Directory

This menu shows various IPsec statistics and errors.

**Read-only arguments**

- `in-errors` (num): Number of input error events.
- `in-buffer-errors` (num): Number of input buffer errors.
- `in-header-errors` (num): Number of input header errors.
- `in-no-states` (num): Number of packets dropped due to no matching state.
- `in-state-protocol-errors` (num): Number of input state protocol errors.
- `in-state-mode-errors` (num): Number of input state mode errors.
- `in-state-sequence-errors` (num): Number of input state sequence errors.
- `in-state-expired` (num): Number of input packets with expired state.
- `in-state-mismatches` (num): Number of input state mismatches.
- `in-state-invalid` (num): Number of input packets with invalid state.
- `in-template-mismatches` (num): Number of input template mismatches.
- `in-no-policies` (num): Number of input packets with no matching policy.
- `in-policy-blocked` (num): Number of input packets blocked by policy.
- `in-policy-errors` (num): Number of input policy errors.
- `out-errors` (num): Number of output error events.
- `out-bundle-errors` (num): Number of output bundle errors.
- `out-bundle-check-errors` (num): Number of output bundle check errors.
- `out-no-states` (num): Number of output packets dropped due to no matching state.
- `out-state-protocol-errors` (num): Number of output state protocol errors.
- `out-state-mode-errors` (num): Number of output state mode errors.
- `out-state-sequence-errors` (num): Number of output state sequence errors.
- `out-state-expired` (num): Number of output packets with expired state.
- `out-policy-blocked` (num): Number of output packets blocked by policy.
- `out-policy-dead` (num): Number of output packets with dead policy.
- `out-policy-errors` (num): Number of output policy errors.
