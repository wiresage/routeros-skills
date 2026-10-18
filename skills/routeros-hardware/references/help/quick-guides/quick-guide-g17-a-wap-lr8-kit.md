# Quick Guide G17-a - wAP LR8 kit

> Source: https://help.mikrotik.com/docs/spaces/QG/pages/15303333/Quick+Guide+G17-a+-+wAP+LR8+kit
>
> Only on help.mikrotik.com: the manual has no quick guides. The help site is frozen; this page was last edited 2024-02-07. The translations into other languages are omitted; the English guide is complete.

# **Models:** RBwAPR-2nD&R11e-LR8 (wAP LR8 kit)

*[Figure]*

## **EN - English -****Quick Guide**:

> **Note**
>
> *This device needs to be upgraded to RouterOS v7.11 or the latest version to ensure compliance with local authority regulations!*
>
> *It is the end user's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.*

*This "wAP LR8" series Quick Guide covers models: RBwAPR-2nD&R11e-LR8 (wAP LR8 kit).*

*This is Wireless Network Device. You can find the product model name on the case label (ID). *[Figure]**

*Please visit the user manual page on <https://mt.lv/um> for the full up-to-date user manual. Or scan the QR code with your mobile phone.*

*Technical specifications, brochures, and more info about products at <https://mikrotik.com/products>*

*The most important technical specifications for this product can be found on the last page of this Quick Guide.*

*Configuration manual for software in your language with additional information can be found at <https://mt.lv/help>*

*MikroTik devices are for professional use. If you do not have qualifications please seek a consultant <https://mikrotik.com/consultants>*

*This Device accepts input from a 24V DC power adapter, which is provided in the original packaging of this device.*

**First steps:**

- Make sure your ISP is allowing hardware change and will issue an automatic IP address;
- Open the bottom lid;
- Connect an external antenna to the SMA connector;
- Connect the device to the power source;
- Connect your ISP cable to the Ethernet port;
- Navigate to the network connections section on your computer and locate the wireless network named *"MikroTik-..."*. Proceed to connect to it (check the wireless passwords on the sticker);
- Configure via a wireless network using a mobile app. Alternatively, use a web browser through *WebFig*or the *Winbox*configuration tool <https://mt.lv/winbox>;
- Download and open *Winbox*, and choose the *Neighbors*tab to find the device;
- The default IP address is 192.168.88.1. Click on the IP address. If the IP is not available, use *Winbox*and connect using the MAC address. The username is *"admin"* and there is no password(or, for some models, check user and wireless passwords on the sticker);
- Click the "Check for updates" button and update RouterOS to the latest version;
- For a manual update of the device, visit the products page at <https://mikrotik.com/products> to find your product. The required packages are accessible under the *"Support&Downloads"* menu;
- Upload downloaded packages to the *WebFig**or* *Winbox* *"Files"* menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- In the *"QuickSet"* menu set up the following: Choose your country, to apply country regulation settings;
- Set up your wireless network password in the left field;
- Set up your router password in the bottom field;
- Find *LR Gateway ID* on the label within the product and register it in your Network Server.

**Safety Information:**

- Before you work on any MikroTik equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents. The installer should be familiar with network structures, terms, and concepts.
- Use only the power supply and accessories approved by the manufacturer, which can be found in the original packaging of this product.
- This equipment is to be installed by trained and qualified personnel, as per these installation instructions. The installer is responsible for making sure, that the Installation of the equipment is compliant with local and national electrical codes. Do not attempt to disassemble, repair, or modify the device.
- This product can be installed outdoors. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware and configuration or to follow the correct procedures could result in a hazardous situation for people and damage to the system.
- The socket-outlet shall be installed near the equipment and shall be easily accessible.
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power adapter from the power outlet.
- To avoid contamination of the environment, separate the device from household waste and dispose of it in a safe manner, for example, in designated areas. Become familiar with procedures for properly transporting the equipment to designated collection points in your area.
- This is a Class A product. In a domestic environment, this product might cause radio interference in which case the user might be required to take adequate measures

**Exposure to Radio Frequency Radiation:**This MikroTik equipment complies with the European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 20 centimeters from your body, occupational user, or the general public.

Manufacturer: Mikrotikls SIA, Unijas iela 2, Riga, Latvia, LV1039.

**BG - Български. Бързо ръководство**:

> **Note**
>
> *Това устройство трябва да бъде надстроено до RouterOS v7.11 или най-новата версия, за да се гарантира спазването на местните регулаторни разпоредби.*
>
> *Крайните потребители са отговорни за спазването на местните разпоредби, включително работата в рамките на законни честотни канали, извеждане на продукция**изисквания за захранване, окабеляване и изисквания за динамичен избор на честота (DFS).* *Всички радиоустройства на MikroTik трябва да бъдат**професионално инсталиран.*

*Това бързо ръководство за серия "wAP LR8" обхваща модели: RBwAPR-2nD & R11e-LR8 (WAP LR8 kit).*

*Това е устройство за безжична мрежа.* *Можете да намерите името на модела на продукта на етикета на регистъра (ID).*[Figure]**

*Моля, посетете страницата с ръководството за потребителя на [https://mt.lv/um](https://translate.googleusercontent.com/translate_c?depth=1&rurl=translate.google.com&sl=en&sp=nmt4&tl=bg&u=https://mt.lv/um&xid=17259,15700022,15700186,15700191,15700259,15700271&usg=ALkJrhgMo9eAlPEIyOhAFnXIc_cSlEZLTQ)[-bg](https://mt.lv/um-bg) за пълното актуализирано ръководство за употреба. Или сканирайте QR кода с мобилния си телефон.*

*Технически спецификации, брошури и повече информация за продуктите на [https://mikrotik.com/products](https://translate.googleusercontent.com/translate_c?depth=1&rurl=translate.google.com&sl=en&sp=nmt4&tl=bg&u=https://mikrotik.com/products&xid=17259,15700022,15700186,15700191,15700259,15700271&usg=ALkJrhhW1tyShmK9J3Pl2xWD1pse6QDCkA)*

*Най-важните технически спецификации за този продукт могат да бъдат намерени на последната страница на това Кратко ръководство.*

*Ръководство за конфигуриране на софтуер на вашия език с допълнителна информация можете да намерите на [https://mt.lv/help](https://translate.googleusercontent.com/translate_c?depth=1&rurl=translate.google.com&sl=en&sp=nmt4&tl=bg&u=https://mt.lv/help&xid=17259,15700022,15700186,15700191,15700259,15700271&usg=ALkJrhgfoOm7FMTeg3wlGwT44bVOxS1BrA)[-bg](https://mt.lv/help-bg)*

*Устройствата MikroTik са за професионална употреба. Ако нямате квалификация, моля, потърсете консултант [https://mikrotik.com/consultants](https://translate.googleusercontent.com/translate_c?depth=1&rurl=translate.google.com&sl=en&sp=nmt4&tl=bg&u=https://mikrotik.com/consultants&xid=17259,15700022,15700186,15700191,15700259,15700271&usg=ALkJrhj3vCzONY6yVbtbkIQVzlnWEp4UgA)*

Това устройство приема вход на 24V DC адаптер за захранване, който се предлага в оригиналната опаковка на това устройство.

**Първи стъпки:**

- Уверете се, че вашият интернет доставчик позволява промяна на хардуера и ще издаде автоматичен IP адрес;
- Отворете долния капак;
- Свържете външна антена към SMA конектора;
- Свържете устройството към източника на захранване;
- Свържете вашия ISP кабел към Ethernet порта;
- Отидете до секцията за мрежови връзки на вашия компютър и намерете безжичната мрежа с име *"MikroTik-..."*. Продължете да се свързвате с него ( проверете безжичните пароли на стикера);
- Конфигурирайте чрез безжична мрежа с помощта на мобилно приложение. Като алтернатива можете да използвате уеб браузър чрез *WebFig* или инструмента за конфигуриране *Winbox* <https://mt.lv/winbox>;
- Изтеглете и отворете *Winbox* и изберете раздела *Neighbors*, за да намерите устройството;
- IP адресът по подразбиране е 192.168.88.1. Кликнете върху IP адреса. Ако IP не е наличен, използвайте *Winbox* и се свържете с MAC адреса. Потребителското име е *"admin"* и няма парола (или, за някои модели, проверете потребителските и безжичните пароли на стикера);
- Щракнете върху бутона *"Check for updates"* и актуализирайте RouterOS до най-новата версия;
- За ръчна актуализация на устройството посетете страницата с продукти на  <https://mikrotik.com/products>, за да намерите вашия продукт. Необходимите пакети са достъпни в менюто *"Support&Downloads"*;
- Качете изтеглените пакети в менюто *WebFig**или**Winbox**"Files"* и рестартирайте устройството;
- Чрез надграждане на софтуера на RouterOS до най-новата версия можете да осигурите оптимална производителност, стабилност и актуализации за сигурност;
- В менюто *"QuickSet"* настройте следното: Изберете вашата страна, за да приложите настройките за регулиране на страната;
- Настройте паролата за вашата безжична мрежа в лявото поле;
- Задайте паролата на вашия рутер в долното поле;
- Намерете *LR Gateway ID* на етикета в продукта и го регистрирайте във вашия мрежов сървър.

**Информация за безопасност:**

- Преди да работите с всяко оборудване на MikroTik, имайте предвид опасностите, свързани с електрическата верига, и се запознайте със стандартните практики за предотвратяване на злополуки.  Инсталаторът трябва да е запознат с мрежовите структури, термини и понятия.
- Използвайте само захранването и аксесоарите, одобрени от производителя, и които можете да намерите в оригиналната опаковка на този продукт.
- Това оборудване трябва да се монтира от обучен и квалифициран персонал съгласно тези инструкции за монтаж.  Инсталаторът отговаря за това, че инсталирането на оборудването е в съответствие с местните и националните електрически кодове.  Не се опитвайте да разглобявате, ремонтирате или модифицирате устройството.
- Този продукт може да бъде инсталиран на открито.  Моля, прочетете внимателно инструкциите за монтаж преди да започнете инсталирането.  Ако не използвате правилния хардуер и конфигурация или не спазвате правилните процедури, това може да доведе до опасна ситуация за хората и да повреди системата.
- Не можем да гарантираме, че няма злополуки или повреди поради неправилна употреба на устройството.  Моля, използвайте внимателно този продукт и работете на свой риск!
- Контактът трябва да бъде монтиран близо до оборудването и да бъде лесно достъпен.
- В случай на повреда на устройството, моля, изключете го от захранването.  Най-бързият начин да направите това е чрез изключване на захранващия адаптер от контакта.
- За да избегнете замърсяване на околната среда, отделете устройството от битовите отпадъци и го изхвърлете по безопасен начин, например на определени места. Запознайте се с процедурите за правилно транспортиране на оборудването до определените пунктове за събиране във вашия район.
- Това е продукт от клас А. В домашна среда този продукт може да причини радиосмущения, в този случай от потребителя може да се наложи да предприеме адекватни мерки.

**Излагане на радиочестотно излъчване:**Това оборудване MikroTik отговаря на ограниченията за радиация на радиационната радиация Европейския съюз, определени за неконтролирана среда.Това устройство MikroTik трябва да бъде инсталирано и експлоатирано на не по-малко от 20 сантиметра от вашето тяло, професионален потребител или широката общественост.

Производител: Mikrotikls SIA, Unijas iela 2, Рига, Латвия, LV1039.

## ***[Figure]***

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/quick-guide-g17-a-wap-lr8-kit.md](../../regulatory/quick-guide-g17-a-wap-lr8-kit.md).
