# Remote access to a LMT Mikrotik router

> Source: https://help.mikrotik.com/docs/spaces/RKB/pages/240156678/Remote+access+to+a+LMT+Mikrotik+router
>
> Only on help.mikrotik.com: the manual has no equivalent page. The help site is frozen; this page was last edited 2024-03-13.

To allow remote access to a MikroTik router, you can follow these steps:

- **Access MikroTik Router:** Connect to your MikroTik router using Winbox, SSH, or the web interface.
- If a remote IP address is known an IP address List can be created. You can also skip this part, but its not recommended.
- **Create an Address List:** In the "IP" menu, go to "Firewall" and then "Address Lists." Click on the "+" button to add a new address list.

*[Figure]*

- **Name:** Provide a name for your address list (e.g., "RemoteAccessList").
- **Address:** Add the IP addresses you want to allow remote access for. You can enter a single IP address, a range, or a subnet.
- **Press ok.**

*[Figure]*

- **Create Firewall Rule:** In the "IP" menu, go to "Firewall" and then "Filter Rules." Click on the "+" button to Add a new rule:

*[Figure]*

- **Rule:** Allow Remote Access for the Address List

*[Figure]*

- **Chain:** input
- **Protocol:** tcp
- **Dst. Port:** The port you want to use for remote access (e.g., 22 for SSH, 8291 for Winbox, 80 for WebFig, 443 for HTTPS)
- **In. Interface:** ether1 (or the interface connected to your external network)
- **Src. Address List:** Choose the address list you created in step 2 or leave it empty - not recommended.
- Click "**Action**" tab and choose **Action**, accept:

*[Figure]*

- **Press ok.**
- **Firewall rule will be created on bottom of the list, use drag n drop and p****lace new rule on top of the list, ip firewall checks connections accordingly starting from 0 rule, if your default: drop all not coming from LAN- rule will be in front of access rule, it will not work.**

*[Figure]*

- To enhance security, you might want to consider restricting access further:
  - Change the default username and password.
  - Consider changing the default port for services like SSH, Winbox.
  - If possible, restrict access to specific source IP addresses.
    **For more information check RouterOS manual.**
- **Testing:** Test the remote access by connecting from a device with one of the specified IP addresses.

Remember to adapt the settings based on your specific requirements and security policies. Always follow best practices to secure remote access to your network devices. Additionally, consider using VPNs for secure remote access.

## Related articles

[Building Advanced Firewall](https://help.mikrotik.com/docs/pages/viewpage.action?pageId=328513)

- [Remote access to a LMT Mikrotik router](https://help.mikrotik.com/docs/spaces/RKB/pages/240156678/Remote+access+to+a+LMT+Mikrotik+router)
- [How to block specific IP address?](https://help.mikrotik.com/docs/spaces/RKB/pages/6488065/How+to+block+specific+IP+address)
