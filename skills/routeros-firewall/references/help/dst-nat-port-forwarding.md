# DST-NAT port forwarding

> Source: https://help.mikrotik.com/docs/spaces/RKB/pages/35946536/DST-NAT+port+forwarding
>
> Only on help.mikrotik.com: the manual has no equivalent page. The help site is frozen; this page was last edited 2020-08-19.

Lai novirzītu noteiktus pieprasījumus uz iekšējā tīkla konkrētu adresi, izmantojiet dst-nat, sekojiet zemāk minētajiem soļiem:

1. Kad ir izveidots savienojums ar iekārtu, izvēlieties WebFig;
2. Dodieties uz IP, Firewall sadaļu;
3. Atveriet NAT cilni;
4. Izveidojiet jaunu ierakstu, nospiežot Add New;
   *[Figure]*
5. Atvērsies jauns logs un aizpildiet sekojošos laukus:
   *[Figure]*
6. Chain, izvēlieties dstnat, jo tiks mainīta saņēmēja IP adrese;
7. Izvēlieties protokolu, piemēram TCP;
8. Dst. Port, norādiet portu, kurš tiks pārsūtīts, piemēram ports 80;
9. In. Interface List norādiet to ienākošo interfeisu uz kuru attieksies konkrētais noteikums, šinī gadījumā tas ir WAN;
10. Dodieties uz lapas apakšu, līdz sadaļai Action;
    *[Figure]*
11. Action, izvēlieties dst-nat;
12. Ievadiet vajadzīgo adresi uz kuru vēlaties pārvirzīt datus;
13. Ievadiet vajadzīgo portu.

> **Info**
>
> Šis izveidotais noteikums var tikt tulkots sekojoši: Kad ienākošais savienojums ar protokolu TCP pieprasa portu 80, veikt saņēmēja adreses tulkošanu un novirzīt to uz vietējo adresi 192.168.1.1 un portu 80.

## Related articles

**Content by label**

There is no content with the specified labels
