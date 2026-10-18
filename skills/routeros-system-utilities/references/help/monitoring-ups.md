# Monitoring UPS

> Source: https://help.mikrotik.com/docs/spaces/RKB/pages/35946519/Monitoring+UPS
>
> Only on help.mikrotik.com: the manual has no equivalent page. The help site is frozen; this page was last edited 2020-08-18.

Items needed for the setup:

1) A Mikrotik device with a USB or RS232 port;
2) USB or RS232 cable;
3) APC UPS with a USB port.

## Step-by-step guide

Connecting and configuring the device.

1. Connect your MikroTik device with your computer;
2. Connect a USB or RS232 cable from your MikroTik device to your APC UPS;
3. Go to System > Packages, check if UPS package is installed, if not, you can find the packages on <https://www.mikrotik.com/download>;
4. Go to System > UPS, click add button;
5. Enter the name of the UPS;
6. Select port;
7. Set offline time and min run time, depending on the device model;
8. Set the preferred alarm setting.

Configuring alarm monitor.

1. Go to System > Logging and choose Actions tab, click, add button;
2. Add a name, type: email, add preferred e-mail address;
3. Select the Rules tab, click add;
4. Choose Topics: UPS, select Action: email.

> **Info**
>
> To configure email, <https://wiki.mikrotik.com/wiki/Manual:Tools/email>
>
> UPS manual, <https://wiki.mikrotik.com/wiki/Manual:System/UPS>

## Related articles

- [Monitoring UPS](https://help.mikrotik.com/docs/spaces/RKB/pages/35946519/Monitoring+UPS)
