# Port forwarding

> Source: https://help.mikrotik.com/docs/spaces/RKB/pages/154042388/Port+forwarding
>
> Only on help.mikrotik.com: the manual has no equivalent page. The help site is frozen; this page was last edited 2022-10-24.

To redirect specific requests to a specific address on the internal network, use dst-nat, follow the steps below:

1. Once connected to the machine, select WebFig;
2. Go to IP, Firewall section;
3. Open the NAT tab;
4. Create a new record by pressing Add New;
   *[Figure]*
5. A new window will open and fill in the following fields:
   *[Figure]*
6. Chain, choose dstnat because the IP address of the recipient will be changed;
7. Select a protocol such as TCP;
8. Dst. Port, specify the port that will be forwarded, for example port 80;
9. In. In the Interface List, indicate the incoming interface to which the specific rule will apply, in this case it is WAN;
10. Go to the bottom of the page, to the Action section;
    *[Figure]*
11. Action, select dst-nat;
12. Enter the desired address to which you want to forward the data;
13. Enter the required port.

This established rule can be translated as follows: When an incoming connection with the TCP protocol requests port 80, translate the recipient's address and redirect it to the local address 192.168.1.1 and port 80.
