# Quick Guide - PWR-LINE AP series

> Source: https://help.mikrotik.com/docs/spaces/QG/pages/14222349/Quick+Guide+-+PWR-LINE+AP+series
>
> Only on help.mikrotik.com: the manual has no quick guides. The help site is frozen; this page was last edited 2022-09-08. The translations into other languages are omitted; the English guide is complete.

# **Models:** PL7411-2nD (EU Plug), PL6411-2nD (US Plug)

*[Figure]*

# **EN - English -** **Quick Guide**:

> **Note**
>
> *This device needs to be upgraded to RouterOS v7.3.1 or the latest version to ensure compliance with local authority regulations!*
>
> *It is the end users' responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.*

*This "PWR-LINE AP" series Quick Guide covers models: PL7411-2nD (EU Plug), PL6411-2nD (US Plug).*

*This is a wireless network device. You can find the product model name on the case label (ID). *[Figure]**

*Please visit the user manual page on <https://mt.lv/um> for the full up-to-date user manual. Or scan the QR code with your mobile phone.*

*Technical specifications, brochures, and more info about products at <https://mikrotik.com/products>*

*The most important technical specifications for this product can be found on the last page of this Quick Guide.*

*Configuration manual for software in your language with additional information can be found at [https://mt.lv/helpPRC](https://mt.lv/help)*

*MikroTik devices are for professional use. If you do not have qualifications please seek a consultant <https://mikrotik.com/consultants>*

The device accepts powering directly from the 100-240 V ~50/60Hz wall socket it is plugged into. The power consumption under maximum load can reach 7 W.

**First steps:**

- Plug both devices into power sockets.
- The main device should be plugged into one of the LAN ports of a router.
- Other devices can be placed anywhere in any sockets in the same power circuit.
- Download the WinBox configuration tool and use the "Neighbors" tab to discover the addresses of the PWR LINE units.
- User name: admin and there is no password by default (or, for some models, check user and wireless passwords on the sticker).
- Make sure the device has an active Internet connection and upgrade to the latest RouterOS version.
- Set up your country, to make sure local regulations are observed.
- To add more devices that will connect over the electrical lines, add compatible devices somewhere in the
  same electrical circuit.
- Hold Sync button 0.5 – 3 seconds to communicate with another device on the Network. The Orange LED light indicates, that it's in search mode.

**Safety Information:**

- Before you work on any MikroTik equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents. The installer should be familiar with network structures, terms, and concepts.
- This equipment is to be installed by trained and qualified personnel, as per these installation instructions. The installer is responsible for making sure, that the Installation of the equipment is compliant with local and national electrical codes. Do not attempt to disassemble, repair, or modify the device.
- This product is intended to be installed indoors. Keep this product away from water, fire, humidity, or hot environments.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the device from the power outlet.

*[Figure]* Electric shock hazard. This equipment is to be serviced by trained personnel only.

**Exposure to Radio Frequency Radiation:**This MikroTik equipment complies with the FCC, IC, and European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 20 centimeters from your body, occupational user, or the general public.

Manufacturer: Mikrotikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039.

## **Note:**

English, For some models, check the user and wireless passwords on the sticker.

Bulgarian, За някои модели проверете потребителската и безжичната парола на стикера.

Czech, U některých modelů zkontrolujte uživatelské a bezdrátové heslo na štítku.

Danish, For nogle modeller skal du kontrollere bruger- og trådløs adgangskoder på mærkaten.

German, Überprüfen Sie bei einigen Modellen die Benutzer- und Wireless-Passwörter auf dem Aufkleber.

Greek, Για ορισμένα μοντέλα, ελέγξτε τους κωδικούς πρόσβασης χρήστη και ασύρματης σύνδεσης στο αυτοκόλλητο.

Spanish, Para algunos modelos, verifique las contraseñas de usuario e inalámbricas en la etiqueta.

Estonian, Mõne mudeli puhul kontrollige kleebis olevaid kasutaja- ja traadita ühenduse paroole.

Finnish, Joissakin malleissa tarkista käyttäjän ja langattoman verkon salasanat tarrasta.

French, Pour certains modèles, vérifiez les mots de passe utilisateur et sans fil sur l'autocollant.

Croatian, Za neke modele provjerite korisničku i bežičnu lozinku na naljepnici.

Hungarian, Egyes modelleknél ellenőrizze a felhasználói és vezeték nélküli jelszavakat a matricán.

Italian, Per alcuni modelli, controlla le password utente e wireless sull'adesivo.

Icelandic, Athugaðu notanda- og þráðlausa lykilorðin á límmiðanum fyrir sumar gerðir.

Norwegian, For noen modeller, sjekk bruker- og trådløse passord på klistremerket.

Lithuanian, Kai kuriuose modeliuose patikrinkite vartotojo ir belaidžio ryšio slaptažodžius ant lipduko.

Latvian, Dažiem modeļiem pārbaudiet lietotāja un bezvadu tīkla paroles uz uzlīmes.

Maltese, Għal xi mudelli, iċċekkja l-utent u l-passwords mingħajr fili fuq l-istiker.

Dutch, Controleer bij sommige modellen de gebruikers- en draadloze wachtwoorden op de sticker.

Polish, W przypadku niektórych modeli sprawdź hasło użytkownika i hasło do sieci bezprzewodowej na naklejce.

Portuguese, Para alguns modelos, verifique as senhas de usuário e sem fio no adesivo.

Romanian, Pentru unele modele, verificați parolele de utilizator și wireless pe autocolant.

Slovak, Pri niektorých modeloch skontrolujte používateľské a bezdrôtové heslá na nálepke.

Slovenian, Pri nekaterih modelih preverite uporabniška in brezžična gesla na nalepki.

Swedish, För vissa modeller, kontrollera användar- och trådlösa lösenord på klistermärket.

Chinese, 对于某些型号，请检查标签上的用户密码和无线密码。

Russian, Для некоторых моделей проверьте пользовательские и беспроводные пароли на наклейке.

Ukrainian, Для деяких моделей перевірте пароль користувача та пароль бездротової мережі на наклейці.

## ***[Figure]***

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/quick-guide-pwr-line-ap-series.md](../../regulatory/quick-guide-pwr-line-ap-series.md).
