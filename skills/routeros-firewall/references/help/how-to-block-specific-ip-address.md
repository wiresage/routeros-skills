# How to block specific IP address?

> Source: https://help.mikrotik.com/docs/spaces/RKB/pages/6488065/How+to+block+specific+IP+address
>
> Only on help.mikrotik.com: the manual has no equivalent page. The help site is frozen; this page was last edited 2020-09-17.

In order to block a specific IP address, you need to add a Firewall filter rule.

## Step-by-step guide

Follow these steps to add filter rule using Winbox:

1. Go to IP>Firewall;
2. Select tab "Filter rules";
3. Click on the + to add new rule;
4. Select tab "General";
5. Choose Chain: Input;
6. Select Src. Address - input your desired IP;
7. Select tab "Action";
8. Choose Action: Drop;
9. Click OK, and the desired IP address will be blocked by a firewall filter.

> **Info**
>
> /ip firewall filter add chain=input src-address=1.1.1.1 action=drop

> **Note**
>
> Chain "input" limit the connection to the device itself. To limit traffic going through the device use chain "forward". Please refer to the [Building Your First Firewall](https://help.mikrotik.com/docs/pages/viewpage.action?pageId=328231)

## Related articles

- [How to install WinBox](https://help.mikrotik.com/docs/spaces/RKB/pages/6488069/How+to+install+WinBox)
- [Remote access to a LMT Mikrotik router](https://help.mikrotik.com/docs/spaces/RKB/pages/240156678/Remote+access+to+a+LMT+Mikrotik+router)
- [How to block specific IP address?](https://help.mikrotik.com/docs/spaces/RKB/pages/6488065/How+to+block+specific+IP+address)
