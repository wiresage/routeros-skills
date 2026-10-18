# Security policy

## What counts as a security problem here

This repository contains instructions that AI agents follow and a few helper scripts. A problem is a security problem when
it could make an agent or a user:

- lose control of a router (instructions that open management services to the internet, disable the firewall, or remove
  the rule that protects the session);
- leak secrets (scripts that print or log passwords, keys or tokens, or take them as command-line arguments);
- run attacker-controlled commands (a script that builds a command from untrusted input without quoting, or that disables
  TLS verification by default);
- trust attacker-controlled text (a reference file or generated page that carries instructions aimed at the agent).

Plain mistakes in the documentation that do not fall into these classes are ordinary bugs; open an issue.

## Reporting

Please do not open a public issue for a security problem. Use GitHub's private vulnerability reporting for this
repository: **Security tab, Report a vulnerability**. Include the file, what an agent or user would do with it, and the
impact. If that option is not available, contact a maintainer of the `wiresage` organization directly.

You can expect an acknowledgement within a few days. Fixes are merged into `master` through a pull request
and are described in the commit message.

## Supported versions

Only the current `master`. Skills are installed by copying files, so re-install after you pull a fix.

## Design rules that reduce the risk

- The scripts read secrets from environment variables, not from arguments, and default to read-only actions.
- TLS certificates are verified unless the caller passes an explicit flag.
- The crawlers read only public pages, identify themselves and respect `robots.txt` crawl delays.
- Skills tell the agent to ask for confirmation before commands that reset, reboot, delete or can cut the management
  session.
- Generated references carry a `Source:` link; the originals at manual.mikrotik.com stay authoritative.
