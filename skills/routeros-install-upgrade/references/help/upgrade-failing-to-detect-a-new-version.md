# Upgrade failing to detect a new version

> Source: https://help.mikrotik.com/docs/spaces/RKB/pages/33325062/Upgrade+failing+to+detect+a+new+version
>
> Only on help.mikrotik.com: the manual has no equivalent page. The help site is frozen; this page was last edited 2024-11-07.

## Problem

The device fails to detect a new version or shows a different version than it is available on <https://mikrotik.com/download>.

An example:

```routeros
/system routerboard print
 	   routerboard: yes
        board-name: RB1100AHx4 Dude Edition
             model: RB1100Dx4
     serial-number: 7932077E32C4
     firmware-type: al2
  factory-firmware: 3.36.3
  current-firmware: 7.11.2
  upgrade-firmware: 7.11.2

/system package update check-for-updates
            channel: stable
  installed-version: 7.11.2
     latest-version: 7.11.3
             status: New version is available
```

## Solution

Please make sure your device is resolving correctly our upgrade servers.

Login to your device and follow these steps:

1. :put [:resolve [upgrade.mikrotik.com](http://upgrade.mikrotik.com)]
2. Check what addresses are returned. Must be the following addresses:
   - 159.148.147.251
3. If not, revise your DNS settings, follow the article for more information: [DNS](https://help.mikrotik.com/docs/pages/viewpage.action?pageId=37748767)

## Related articles

- [Downgrading RouterOS](https://help.mikrotik.com/docs/spaces/RKB/pages/328316/Downgrading+RouterOS)
- [Cannot upgrade SwOS](https://help.mikrotik.com/docs/spaces/RKB/pages/15303614/Cannot+upgrade+SwOS)
- [Default password](https://help.mikrotik.com/docs/spaces/RKB/pages/285147143/Default+password)
- [Try Before RMA](https://help.mikrotik.com/docs/spaces/RKB/pages/57475128/Try+Before+RMA)
- [Upgrade failing to detect a new version](https://help.mikrotik.com/docs/spaces/RKB/pages/33325062/Upgrade+failing+to+detect+a+new+version)
