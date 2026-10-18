# Default password

> Source: https://help.mikrotik.com/docs/spaces/RKB/pages/285147143/Default+password
>
> Only on help.mikrotik.com: the manual has no equivalent page. The help site is frozen; this page was last edited 2024-11-27.

## Problem

You have obtained a MikroTik RouterOS powered device, but can't log in, as it asks for a login and password. You have either reset the unit, or have obtained it from somewhere and would like to know the credentials.

## Solution

If the device is not preconfigured with a custom password and has been reset and reinstalled with the Netinstall utility, most likely there is a default login and password. Older MikroTik devices come with the login "admin" and no password out of the box (just type admin in the login prompt, and hit enter when asked for a password). However, newer models do have a default password set in the factory. In some cases, custom branded units could contain a different default password, but those can be reset using the Netinstall utliity.

This password can be found in the following places:

1. On the device itself, on the serial number sticker
2. On the packaging of the device, also on the serial number sticker
3. On the device "Quick Guide" paper sheet, which comes with the unit, usually inside the packaging.
4. The password is also provided to the Main Distributor of MikroTik products, that sold the device. The distributor should have a default password database, so provide them the serial number of the unit, and the seller / shop where you got the device, can provide you with this password. Only attempt this if you have not found any stickers as mentioned above.

## Related articles

- [Default password](https://help.mikrotik.com/docs/spaces/RKB/pages/285147143/Default+password)
- [Lost password](https://help.mikrotik.com/docs/spaces/RKB/pages/8323179/Lost+password)
- [Reset the password](https://help.mikrotik.com/docs/spaces/RKB/pages/328274/Reset+the+password)
