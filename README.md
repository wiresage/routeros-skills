# routeros-skills

Agent skills that teach AI coding agents how to work with MikroTik RouterOS.

Each skill is a folder with a `SKILL.md` (short, task-oriented instructions) and a `references/` folder that holds the
official documentation for that area as plain Markdown. The instructions tell an agent what to do and what to avoid; the
references let it look up the exact command, property or procedure instead of guessing.

The skills use only the portable Agent Skills format: a `name` and a `description` in the front matter, then Markdown.
They work with Claude Code, Codex, GitHub Copilot and any other agent that reads `SKILL.md` folders.

> Status: private, awaiting review. It is meant to become a public repository of the `wiresage` organization and, with
> [routeros-lsp](https://github.com/wiresage/routeros-lsp) and [mikrotik-mcp](https://github.com/wiresage/mikrotik-mcp), the
> knowledge layer of a MikroTik agent.

## Skills

Start with `routeros-fundamentals`; it explains the console conventions and points to the other skills.

| Skill | Covers |
| --- | --- |
| [routeros-fundamentals](skills/routeros-fundamentals/SKILL.md) | CLI syntax, menu hierarchy, safe mode, export and import, v6 versus v7, map of the other skills |
| [routeros-initial-setup](skills/routeros-initial-setup/SKILL.md) | First configuration, default config, WAN and LAN setup, hardening, backup, export, import, reset |
| [routeros-install-upgrade](skills/routeros-install-upgrade/SKILL.md) | Upgrade and downgrade, packages, Netinstall, CHR and x86 installation, RouterBOOT, licensing, v7 migration |
| [routeros-firewall](skills/routeros-firewall/SKILL.md) | Filter, NAT, mangle and raw rules, connection tracking and FastTrack, address lists, packet flow, IPv6 firewall, hardening recipes |
| [routeros-queues](skills/routeros-queues/SKILL.md) | Simple queues and queue trees, HTB, PCQ, CAKE and FQ-CoDel, bursts, queue sizes |
| [routeros-vpn](skills/routeros-vpn/SKILL.md) | WireGuard, L2TP, SSTP, OpenVPN, PPTP, PPPoE, EoIP, GRE, IPIP, 6to4, ZeroTier tunnels |
| [routeros-ipsec](skills/routeros-ipsec/SKILL.md) | IKEv1/IKEv2, policies, peers and identities, certificates and EAP, road warrior and site-to-site examples, troubleshooting |
| [routeros-certificates](skills/routeros-certificates/SKILL.md) | Certificate templates, signing, import and export, ACME and Let's Encrypt, SCEP, CRL, trust stores |
| [routeros-users-aaa](skills/routeros-users-aaa/SKILL.md) | Router users and groups, SSH keys, RADIUS client, PPP profiles and secrets, 802.1X |
| [routeros-routing](skills/routeros-routing/SKILL.md) | Static routes, routing tables and rules, policy routing, VRF, route filters, ECMP, nexthop lookup, RIP, IS-IS, BFD, multicast, v6 to v7 routing migration |
| [routeros-ospf](skills/routeros-ospf/SKILL.md) | OSPFv2 and OSPFv3 instances, areas, interface templates, redistribution, neighbours, area types |
| [routeros-bgp](skills/routeros-bgp/SKILL.md) | BGP connections, templates and sessions, filters, route reflectors, roles and route-leak prevention, RPKI, EVPN |
| [routeros-mpls](skills/routeros-mpls/SKILL.md) | MPLS switching, LDP, VPLS, traffic engineering, MPLS MTU and L3VPN pointers |
| [routeros-bridging-switching](skills/routeros-bridging-switching/SKILL.md) | Bridges, VLAN filtering, STP/RSTP/MSTP, hardware offloading, IGMP snooping, DHCP snooping, VXLAN, MACsec, SwOS, CRS switch chips |
| [routeros-dhcp](skills/routeros-dhcp/SKILL.md) | DHCP server, client, relay, leases, options, DHCPv6 server/client and prefix delegation |
| [routeros-dns](skills/routeros-dns/SKILL.md) | DNS resolver and cache, static entries and forwarders, adlists, DNS over HTTPS, mDNS repeater, DNS update |
| [routeros-ip-addressing](skills/routeros-ip-addressing/SKILL.md) | IPv4 and IPv6 addresses, pools, ARP, neighbor discovery and RAs, SLAAC, kernel IP settings |
| [routeros-network-services](skills/routeros-network-services/SKILL.md) | MikroTik cloud (DDNS, Back To Home, cloud backup, File Share), web proxy, reverse proxy, SOCKS, Socksify, OpenFlow |
| [routeros-ethernet](skills/routeros-ethernet/SKILL.md) | Ethernet and SFP ports, auto-negotiation, forced mode, FEC, MTU and L2MTU, interface lists, PWR-Line |
| [routeros-wireless](skills/routeros-wireless/SKILL.md) | Wi-Fi 5/6/7 (wifi package), legacy wireless, CAPsMAN, Nv2, W60G 60 GHz, regulatory, troubleshooting |

## How a skill is laid out

```text
skills/<name>/
  SKILL.md        instructions: when to use it, workflow, recipes, pitfalls, where to look
  scripts/        optional shell, PowerShell or Python helpers (only when they add value)
  references/     the documentation for this area
    INDEX.md      what is inside, one line per file (start here)
    guides/       narrative pages of the manual, same path as on manual.mikrotik.com
    cli/          the CLI reference; one file per menu, including its commands
    products/     hardware manuals (routeros-hardware only)
    help/         pages that exist only on help.mikrotik.com
```

An agent loads only the `name` and `description` of every skill, reads `SKILL.md` when a task matches, and opens a reference
file only when it needs that detail. Keep that in mind when you write or review a skill: `SKILL.md` should be enough to do
the common task correctly, and the references should be enough to do the rare one.

## Install

Skills are plain folders, so installing means copying or linking them into the place your agent reads skills from. The
installers do that for you:

```bash
scripts/install-skills.sh --target ~/.claude/skills            # every skill
scripts/install-skills.sh --target .agents/skills routeros-firewall routeros-vpn   # selected skills
```

```powershell
scripts/install-skills.ps1 -Target "$HOME\.claude\skills"
```

Common locations (check your agent's documentation, they change): Claude Code `.claude/skills/` or `~/.claude/skills/`,
Codex `.agents/skills/`, GitHub Copilot `.github/skills/`. Use `--link` (`-Link`) to symlink instead of copy so that a
`git pull` updates the installed skills.

## Where the content comes from

| Source | Used for |
| --- | --- |
| [manual.mikrotik.com](https://manual.mikrotik.com) | The primary source: every page in its `llms.txt` index (narrative guides and the CLI reference) and the hardware manuals |
| [help.mikrotik.com/docs](https://help.mikrotik.com/docs) | The older Confluence documentation, which MikroTik has frozen. Used only for pages the manual does not have: quick guides, a few user manuals, knowledge-base articles and a handful of concept pages |

The snapshot date and the page counts are in [docs-snapshot.json](docs-snapshot.json). The crawl, the conversion to
Markdown and the checks that every page arrived complete are part of this repository (see [CONTRIBUTING.md](CONTRIBUTING.md)),
so the snapshot can be refreshed when MikroTik updates the manual.

Not included: the manual's blog and its documentation change log (they are not RouterOS documentation), tag listing pages
(they only repeat links), pictures (each reference has a `Source:` link to the page with the figures), the translations in
the quick guides (the English text is complete), and one help page about exam proctoring. Details are in `docs-snapshot.json`.

## Related projects

- [routeros-lsp](https://github.com/wiresage/routeros-lsp): language server for RouterOS scripts. Use it to check `.rsc` files
  before they reach a router.
- [mikrotik-mcp](https://github.com/wiresage/mikrotik-mcp): MCP server that lets an agent read and change a real device.

The skills in this repository are written so that they also work when the agent has no live access: they tell it which
commands to propose and how to verify them.

## License

The instructions, scripts and tools in this repository are available under the [MIT License](LICENSE).
The documentation copied into the `references/` folders belongs to MikroTik; see [NOTICE.md](NOTICE.md).

See also [AGENTS.md](AGENTS.md) (for agents that work on this repository), [CONTRIBUTING.md](CONTRIBUTING.md) and
[SECURITY.md](SECURITY.md).
