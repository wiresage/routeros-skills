# LMT 5G r4

> Source: https://help.mikrotik.com/docs/spaces/QG/pages/71532549/LMT+5G+r4
>
> Only on help.mikrotik.com: the manual has no quick guides. The help site is frozen; this page was last edited 2021-06-14. The translations into other languages are omitted; the English guide is complete.



## [LMT 5G](https://help.mikrotik.com/docs/display/QG/LMT+5G)

Maršrutētājs ir paredzēts lietošanai mājās vai birojā, tam ir piecas pieslēgvietas jūsu lokālajām ierīcēm un SIM kartes slots SIM kartei. Ierīce spēj nodrošināt 2,4 GHz un 5 GHz bezvadu tīklu.

## Iestatīšana

Lūdzu, veiciet šos soļus, lai iestatītu ierīci:*[Figure]*

- Pievienojiet SMA savienotājam ārējās antenas, skat. "[Antenas lietošana](#)".
  *[Figure]*
- Ievietojiet Micro SIM karti slotā, kas atrodas ierīces apakšpusē.
  *[Figure]*
- Savienojiet datoru ar Ethernet portu – vienu no piecām pieslēgvietām.
- Pievienojiet strāvas adapteri līdzstrāvas ligzdai un iespraudiet kontaktligzdā.
- Kad ierīce ir ieslēgta un savienota ar datoru, atveriet saiti
  [https://192.168.8.1](https://192.168.88.1_) interneta pārlūkprogrammā, lai sāktu konfigurēšanu.
- Lietotājvārds *admin* un parole ir atrodama uz uzlīmes iekārtas aizmugurē.
- Lai personalizētu bezvadu tīklus, jūs varat nomainīt to nosaukumus laukā *Network Name*.
- Iestatiet bezvadu tīkla paroli laukā *WiFi Password*, izmantojiet vismaz astoņus simbolus.
- Iestatiet iekārtas paroli laukā *Password* un ievadiet to atkārtoti laukā
  *Confirm Password*, tā tiks izmantota, lai pieteiktos nākamajā reizē.
- Nospiediet *Apply Configuration*, lai saglabātu izmaiņas.

## Savienojuma izveide ar mobilo lietotni

Izmantojiet viedtālruni, lai piekļūtu maršrutētājam, pieslēdzoties bezvadu tīklam:

- Ievietojiet SIM karti un pieslēdziet ierīci, kā aprakstīts [iestatīšanas](#) sadaļā.*[Figure]*
- Skenējiet QR kodu ar viedtālruni, lai lejupielādētu konfigurācijas lietotni Android vai iPhone ierīcēm.
- Izveidojiet savienojumu ar ierīci, pieslēdzoties 2,4 GHz vai 5 GHz bezvadu tīklam ar nosaukumu LMT-xxxxxx.
- Atveriet mobilo lietotni.
- Pēc noklusējuma IP adrese un lietotājvārds jau būs ievadīti.
- Noklikšķiniet *Connect* (Pieslēgties), lai izveidotu savienojumu ar ierīci caur bezvadu tīklu.
- Izvēlieties *Quick setup* (Ātrā iestatīšana), un lietojumprogramma palīdzēs veikt pamata uzstādījumus pāris soļos.

## Ierīces apraksts

*[Figure]*

1. [Atiestatīšanas poga (reset).](#)
2. [Strāvas adaptera](#) līdzstrāvas ligzda 2.0 mm.
3. Piecas *Gigabit* pieslēgvietas lokālajām ierīcēm.
4. USB slots A tipa.
5. [SIM slots.](#)
6. Režīma poga (mode).
7. [SMA antenu](#) ārējie savienojumi.
8. [Sinhronizācijas poga (WPS).](#)

## Uzstādīšana

Ierīce ir paredzēta lietošanai iekštelpās, novietojot to uz darba virsmas.
Ieteicams izmantot Cat5 aizsargātos kabeļus. Uzstādīt un lietot ierīci tā, lai tā atrastos vismaz 20 cm attālumā no jūsu ķermeņa.

## Barošanas avots

Ierīci ir iespējams ieslēgt, izmantojot strāvas padevi no adaptera:

- Līdzstrāvas tiešās ievades kontaktligzda (5,5 mm ārpusē un 2 mm iekšpusē) 12-28 V.

Jaudas patēriņš maksimālās slodzes apstākļos var sasniegt 17 W. Pieslēdzot, papildpiederumus, tas var palielināties līdz 23 W.

## Konfigurācija

Ieteicams veikt atjauninājumus pēc iespējas biežāk, lai saņemtu jaunāko programmatūras RouterOS versiju, kas nodrošina vislabāko veiktspēju un stabilitāti.
Papildus tam, kas aprakstīts šajā dokumentā, *RouterOS* ietver daudzas konfigurācijas opcijas. Ieteicams skatīt šeit, lai saprastu iespējas: <https://mt.lv/help>. Ja *IP* savienojums nav pieejams, var izmantot *Winbox* rīku (<https://mt.lv/winbox>), lai izveidotu savienojumu ar ierīces *MAC* adresi no *LAN* puses.
Lai atjaunotu sākotnējos iesttījumus, izmantot "[Atiestatīšanas pogu](#)".

#

## Sinhronizācijas poga

Sinhronizācijas poga atrodas ierīces augšpusē. Izmantojiet sinhronizācijas pogu, lai pieslēgtu jaunu ierīci savam bezvadu tīklam:

*[Figure]*

- Lai pieslēgtos 5 GHz tīklam, nospiediet un turiet pogu ne ilgāk par 5 sekundēm;
- Lai pieslēgtos 2,4 GHz tīklam, nospiediet un turiet pogu ilgāk par 5 sekundēm.

## Gaismas indikatori

# *[Figure]*

## SIM slota lietošana

*[Figure]*

SIM kartes slots ir paredzēts lietošanai ar Micro SIM kartēm.
Nano SIM kartēm ir atšķirīgs biezums, to lietošana ar adapteri nav ieteicama.

## Atiestatīšanas poga

Atiestatīšanas pogai ir trīs funkcijas:

- Turiet šo pogu iekārtas ieslēgšanas brīdī, līdz indikators sāk mirgot, tad atlaidiet pogu, un iekārta aktivizēs noklusējuma konfigurāciju.
- Turpiniet turēt pogu līdz indikatora nodzišanai, tad atlaidiet pogu, un iekārta sāks meklēt *Netinstall* serveri.
- Kad ierīce ir ieslēgta, turiet pogu 5–10 sekundes, atlaidiet pogu un ierīce restartēsies, aktivizējot noklusējuma konfigurāciju.

Neatkarīgi no iepriekš veiktajām darbībām sistēma ielādēs dublēto *RouterBOOT loader*, tas ir noderīgs atkļūdošanai un sistēmas atkopšanai

## Piederumi

Komplektā ietilpst šādi ierīces komplektācijā iekļautie piederumi:

- *EU* strāvas pārveidotājs 24 V, 1,2 A.
- *CAT5E UTP* plakanais kabelis 1,5 m.
- *LTE/5G* antenas, 2 gab.

## Antenas lietošana

> **Info**
>
> Pirms pievienojiet antenas, izslēdziet ierīci, pretējā gadījumā ierīce var tikt bojāta!

Ārējo antenu ligzdas atrodas iekārtas aizmugures daļā.

- Pieskrūvējiet abas antenas pie SMA ligzdām (Sekojiet instrukcijām attēlos).

*[Figure]*

## Operētājsistēmas atbalsts

Ierīce atbalsta *RouterOS* programmatūras versiju v7. Konkrētais rūpnīcas instalētās versijas numurs ir norādīts *RouterOS* izvēlnē (system resource). Citas operētājsistēmas nav atbalstītas.

#

## Specifikācijas

- 2,4 GHz (802.11b/g/n) un 5 Ghz (802.11a/n/ac) bezvadu moduļi.

Papildinformāciju par šo produktu, specifikāciju un attēliem skatiet mūsu tīmekļa vietnē: <https://mt.lv/LMT_5G>

## Personas datu apstrāde

SIA "Mikrotīkls", reģistrācijas nr. 40003286799, juridiskā adrese Aizkraukles 23, Rīga (MikroTik), ir apņēmies aizsargāt lietotāju privātumu un personas datus. Kā personas datu apstrādes pārzinis MikroTik veic informācijas, biznesa datu un personas datu apstrādi un nodrošina to aizsardzību saskaņā ar Eiropas Savienības un nacionālajiem normatīvajiem aktiem par datu apstrādes un MikroTik principu aizsardzību personas datu apstrādē.
Jebkura fiziska persona var izmantot datu subjekta tiesības, kas norādītas Vispārīgajā datu aizsardzības regulā (ES regula Nr. 679/2016).
Šeit varat uzzināt vairāk par MikroTik personas datu apstrādes principiem. [https://mikrotik.com/privacy](https://mikrotik.com/privacy%20)

## Protokols TR-069

Lai nodrošinātu tīkla integritāti, drošību un pakalpojumus atbilstīgā kvalitātē, pakalpojumiem nepieciešamo konfigurācijas jautājumu risināšanai un tīkla problēmsituāciju laicīgai diagnosticēšanai iekārtā var būt integrēts tehniskais protokols TR-069, kas nodrošina attiecīgo tīkla parametru (piem., signāla līmeņa, signāla kvalitātes, tīkla šūnas informācijas, izmantotās frekvences, tīkla noslodzes informācijas) apmaiņu iekārtai ar pakalpojumu sniedzēja sistēmām. Apstrāde notiek saskaņā ar piemērojamiem normatīvajiem aktiem un konkrētajam mērķim vajadzīgo laiku. Plašākai informācijai sazinieties ar pakalpojumu sniedzēju.

## Drošības Informācija

- Pirms sākat strādāt ar šo MikroTik aprīkojumu, iepazīstieties ar briesmām, kas saistītas ar elektriskajām shēmām, un iepazīstieties ar standarta praksi negadījumu novēršanā. Instalētājam būtu jāpārzina tīkla struktūras, termini un koncepcijas.
- Izmantojiet tikai ražotāja apstiprinātu barošanas avotu un piederumus, kas atrodami šī produkta oriģinālajā iepakojumā.
- Saskaņā ar šīm uzstādīšanas instrukcijām, šo aprīkojumu jāuzstāda apmācītai un kvalificētai personai. Uzstādītāja pienākums ir pārliecināties, ka aprīkojuma uzstādīšana atbilst Latvijas valsts elektrības noteikumiem. Nemēģiniet ierīci izjaukt, labot vai pārveidot.
- Šis produkts ir paredzēts uzstādīšanai telpās. Sargājiet šo izstrādājumu no ūdens, uguns, mitruma vai karstas vides.
- Mēs nevaram garantēt, ka negadījumi vai bojājumi nenotiks, ja ierīce tiks izmantota nepareizi. Lūdzu, izmantojiet šo produktu uzmanīgi un tikai ražotāja paredzētā veidā.
- Ierīces kļūmes gadījumā, lūdzu, atvienojiet to no strāvas. Ātrākais veids, kā to izdarīt, ir, atvienojot strāvas adapteri no kontaktligzdas.

Radiofrekvences starojuma iedarbība: Šī MikroTik iekārta atbilst Eiropas Savienības radiācijas iedarbības ierobežojumiem, kas noteikti nekontrolētai videi. Šī MikroTik ierīce jāuzstāda un jādarbina ne tuvāk par 20 centimetriem no ķermeņa vai plašas sabiedrības.

**Brīdinājums:** Šis ir B klases produkts. Sadzīves vidē šis produkts var izraisīt radio traucējumus, un tādā gadījumā lietotājam var prasīt veikt atbilstošus pasākumus.

Ražotājs: Mikrotikls SIA, Brīvības gatve 214i Rīga, Latvija, LV1039.

|  |  |
| --- | --- |
| LV | Ar šo Mikrotīkls SIA deklarē, ka radioiekārta D53G-5HacD2HnD-TC&RG502Q-EA atbilst Direktīvai 2014/53/ES. Pilns ES atbilstības deklarācijas teksts ir pieejams šādā interneta vietnē: <https://mikrotik.com/products> |

Šī MikroTik ierīce atbilst maksimālajām pārraides jaudas robežām atbilstoši ETSI noteikumiem. Sīkāku informāciju skatiet iepriekš atbilstības deklarācijā.

Šīs ierīces WLAN funkcija ir ierobežota lietošanai iekštelpās tikai tad, ja tā darbojas frekvenču diapazonā no 5150 līdz 5350 MHz.

###

### ***WLAN / WCDMA / LTE / 5G***

|  |  |  |
| --- | --- | --- |
| Darba frekvence / maksimālā izejas jauda | WLAN 2.4 Ghz | 2400-2483.5 MHz / 20 dBm |
| WLAN 5Ghz | 5150-5250 MHz / 23 dBm |
| WLAN 5Ghz | 5250-5350 MHz / 20 dBm |
| WLAN 5Ghz | 5470-5725 MHz / 27 dBm |
| WCDMA Band I | 1922.4 MHz / 23dBm ± 2.7 dB |
| WCDMA Band III | 1712.4 MHz / 23dBm ± 2.7 dB |
| WCDMA Band V | 826.4 MHz / 23dBm ± 2.7 dB |
| WCDMA Band VIII | 882.4 MHz / 23dBm ± 2.7 dB |
| LTE Band 1 | 2100 MHz / 23dBm ± 2.7 dB |
| LTE Band 3 | 1700 MHz / 23dBm ± 2.7 dB |
| LTE Band 5 | 850 MHz / 23dBm ± 2.7 dB |
| LTE Band 7 | 2600 MHz / 23dBm ± 2.7 dB |
| LTE Band 8 | 900 MHz / 23dBm ± 2.7 dB |
| LTE Band 20 | 800 MHz / 23dBm ± 2.7 dB |
| LTE Band 28 | 700 MHz / 23dBm ± 2.7 dB |
| LTE Band 32 | 1500 MHz / 23dBm ± 2.7 dB |
| LTE Band 34 | 2000 MHz / 23dBm ± 2.7 dB |
| LTE Band 38 | 2600 MHz / 23, 26dBm ± 2.7 dB |
| LTE Band 40 | 2300 MHz / 23, 26dBm ± 2.7 dB |
| LTE Band 41 | 2500 MHz / 23, 26dBm ± 2.7 dB |
| LTE Band 42 | 3500 MHz / 23, 26dBm ± 3 dB |
| LTE Band 43 | 3700 MHz / 23dBm ± 3 dB |
| 5G NR Band n1 | 2100 MHz / 23dBm ± 2 dB |
| 5G NR Band n3 | 1800 MHz / 23dBm ± 2 dB |
| 5G NR Band n7 | 2600 MHz / 23dBm ± 2 dB |
| 5G NR Band n8 | 900 MHz / 23dBm ± 2 dB |
| 5G NR Band n20 | 800 MHz / 23dBm ± 2 dB |
| 5G NR Band n28 | 700 MHz / 23dBm ± 2 dB |
| 5G NR Band n38 | 2600 MHz / 23dBm ± 2 dB |
| 5G NR Band n40 | 2300 MHz / 23dBm ± 2 dB |
| 5G NR Band n41 | 2500 MHz / 26dBm ± 2 dB |
| 5G NR Band n77 | 3700 MHz / 26dBm ± 2 dB |
| 5G NR Band n78 | 3500 MHz / 26dBm ± 2 dB |

#62998
