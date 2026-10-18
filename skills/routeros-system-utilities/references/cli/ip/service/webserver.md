# /ip/service/webserver

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/service/webserver

Type: Settings Directory

Turns individual parts of the router's web server on or off, separately for HTTP (the `-plain` settings, served by the `www` service) and HTTPS (the `-secure` settings, served by `www-ssl`). All parts are enabled by default. A disabled part answers `403 Forbidden`, and the other parts keep working, so you can, for example, offer the REST API over HTTPS without WebFig. The port, allowed addresses and certificate of the web server are set in [`/ip/service`](../service.md). For the REST API, see [REST API](https://manual.mikrotik.com/docs/developer-guides/rest-api).

**Arguments**

- `index-plain` (bool): Home page (login page) and static files such as `/favicon.png` over HTTP. Takes effect only when `webfig-plain` and `graphs-plain` are also `no`; then the home page, static files and unknown paths answer 403 over HTTP, and the REST API keeps working. Default: yes.
- `webfig-plain` (bool): WebFig at `/webfig/` over HTTP. Default: yes.
- `graphs-plain` (bool): Graphs at `/graphs/` over HTTP. Default: yes.
- `rest-plain` (bool): [REST API](https://manual.mikrotik.com/docs/developer-guides/rest-api) at `/rest` over HTTP. With `no`, REST requests over HTTP answer 403, and HTTPS is not affected. Default: yes.
- `crl-plain` (bool): Certificate revocation list downloads at `/crl/` over HTTP. Default: yes.
- `scep-plain` (bool): SCEP server at `/scep/` over HTTP. Default: yes.
- `acme-plain` (bool): Answers to ACME HTTP-01 challenge requests at `/.well-known/acme-challenge/` over HTTP. Default: yes.
- `index-secure` (bool): Home page (login page) and static files such as `/favicon.png` over HTTPS. Takes effect only when `webfig-secure` and `graphs-secure` are also `no`; then the home page and static files answer 403 over HTTPS, and the REST API keeps working. Default: yes.
- `webfig-secure` (bool): WebFig at `/webfig/` over HTTPS. Default: yes.
- `graphs-secure` (bool): Graphs at `/graphs/` over HTTPS. Default: yes.
- `rest-secure` (bool): [REST API](https://manual.mikrotik.com/docs/developer-guides/rest-api) at `/rest` over HTTPS. With `no`, REST requests over HTTPS answer 403, and HTTP is not affected. Default: yes.
