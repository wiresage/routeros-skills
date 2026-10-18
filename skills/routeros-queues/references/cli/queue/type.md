# /queue/type

> Source: https://manual.mikrotik.com/docs/cli-reference/queue/type

Type: Directory

**Flags**

- `*`: default

**Arguments**

- `name` (string; mandatory)
- `kind` (enum: bfifo | pfifo | red | sfq | pcq | mq-pfifo | none | codel | fq-codel | cake; mandatory)
- `bfifo-limit` (num)
- `pfifo-limit` (num)
- `red-limit` (num)
- `red-min-threshold` (num)
- `red-max-threshold` (num)
- `red-burst` (num)
- `red-avg-packet` (num)
- `sfq-perturb` (num)
- `sfq-allot` (num)
- `pcq-rate` (num)
- `pcq-limit` (num)
- `pcq-classifier` (ubit (src-address, dst-address, src-port, dst-port))
- `pcq-total-limit` (num)
- `pcq-burst-rate` (num)
- `pcq-burst-threshold` (num)
- `pcq-burst-time` (time)
- `pcq-src-address-mask` (num)
- `pcq-dst-address-mask` (num)
- `pcq-src-address6-mask` (num)
- `pcq-dst-address6-mask` (num)
- `mq-pfifo-limit` (num)
- `codel-limit` (num)
- `codel-interval` (time)
- `codel-target` (time)
- `codel-ecn` (bool)
- `codel-ce-threshold` (time)
- `fq-codel-limit` (num)
- `fq-codel-interval` (time)
- `fq-codel-target` (time)
- `fq-codel-ecn` (bool)
- `fq-codel-ce-threshold` (time)
- `fq-codel-flows` (num)
- `fq-codel-memlimit` (num)
- `fq-codel-quantum` (num)
- `cake-bandwidth` (num)
- `cake-autorate-ingress` (bool)
- `cake-overhead` (num)
- `cake-mpu` (num)
- `cake-atm` (enum: none | atm | ptm)
- `cake-overhead-scheme` (multi { cake-overhead-scheme: enum (raw | conservative | ipoa-vcmux | ipoa-llcsnap | bridged-vcmux | bridged-llcsnap | pppoa-vcmux | pppoa-llc | pppoe-vcmux | pppoe-llcsnap | pppoe-ptm | bridged-ptm | via-ethernet | ethernet | ether-vlan | docsis) })
- `cake-rtt` (time)
- `cake-rtt-scheme` (enum: none | datacentre | lan | metro | regional | internet | oceanic | satellite | interplanetary)
- `cake-diffserv` (enum: diffserv3 | diffserv4 | diffserv8 | besteffort | precedence)
- `cake-flowmode` (enum: flowblind | srchost | dsthost | hosts | flows | dual-srchost | dual-dsthost | triple-isolate)
- `cake-nat` (bool)
- `cake-wash` (bool)
- `cake-ack-filter` (enum: none | filter | aggressive)
- `cake-memlimit` (num)
