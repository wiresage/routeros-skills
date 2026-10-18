# /routing/filter/select-rule

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/filter/select-rule

Type: Directory

**Flags**

- `X`: disabled
- `I`: invalid

**Arguments**

- `chain` (enum; mandatory; unset)
- `do-where` (enum; unset)
- `do-group-num` (super { prop: enum (distance | scope | target-scope | dst-len | bgp-weight | bgp-med | bgp-out-med | bgp-local-pref | bgp-path-len | bgp-path-prepend | bgp-path-peer-prepend | bgp-input-local-as | bgp-input-remote-as | bgp-output-local-as | bgp-output-remote-as | ospf-metric | ospf-tag | ospf-ext-metric | ospf-ext-tag | rip-metric | rip-tag | rip-ext-metric | rip-ext-tag) , [chain] >enum }; unset)
- `do-group-prfx` (super { prop: enum (dst | gw | pref-src | ospf-fwd | ospf-fwd | bgp-input-local-addr | bgp-input-remote-addr | bgp-output-local-addr | bgp-output-remote-addr) , [chain] >enum }; unset)
- `do-select-num` (super { prop: enum (distance | scope | target-scope | dst-len | bgp-weight | bgp-med | bgp-out-med | bgp-local-pref | bgp-path-len | bgp-path-prepend | bgp-path-peer-prepend | bgp-input-local-as | bgp-input-remote-as | bgp-output-local-as | bgp-output-remote-as | ospf-metric | ospf-tag | ospf-ext-metric | ospf-ext-tag | rip-metric | rip-tag | rip-ext-metric | rip-ext-tag) , [compare] >enum (largest-none-best | largest-none-worst | smallest-none-best | smallest-none-worst) }; unset)
- `do-select-prfx` (super { prop: enum (dst | gw | pref-src | ospf-fwd | ospf-fwd | bgp-input-local-addr | bgp-input-remote-addr | bgp-output-local-addr | bgp-output-remote-addr) , [compare] >enum (largest-none-best | largest-none-worst | smallest-none-best | smallest-none-worst) }; unset)
- `do-take` (num)
- `do-jump` (enum)
