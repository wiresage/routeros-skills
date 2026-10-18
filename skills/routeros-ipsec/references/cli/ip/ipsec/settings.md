# /ip/ipsec/settings

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/ipsec/settings

Type: Settings Directory

**Arguments**

- `xauth-use-radius` (bool): Whether to use Radius client for XAuth users or not. The property is only applicable to peers using the IKEv1 exchange mode.
- `accounting` (bool): WWhether to send RADIUS accounting requests to a RADIUS server. Applicable if EAP Radius (auth-method=eap-radius) or pre-shared key with XAuth authentication method (auth-method=pre-shared-key-xauth) is used.
- `interim-update` (time): The interval between each consecutive RADIUS accounting Interim update. Accounting must be enabled.
- `ddos-cookie-threshold` (num): DDOS cookie activation threshold.
