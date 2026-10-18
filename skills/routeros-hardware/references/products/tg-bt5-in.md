# TG-BT5-IN

> Source: https://manual.mikrotik.com/hardware/tg-bt5-in
>
> Category: IoT products

This guide can be downloaded as a [PDF file](https://manual.mikrotik.com/assets/files/tg-bt5-in-c808773bd63bcc571c9cefe268e5bc79.pdf).

*[Figure]*

TG-BT5-IN is ready to use Bluetooth Tag with a preinstalled battery. The software manual you can find under each product in the Support and Downloads sections <https://mikrotik.com/products>. See the [TG-BT5-IN product page](https://mikrotik.com/product/tg_bt5_in) for full specifications and brochures.

## Software-related links

You can find the guide on how to configure the tag using the Android app following the link:

MikroTik Beacon Manager for Android devices

You can find the guide on how to configure the tag using the iOS app following the link:

MikroTik Beacon Manager for iOS devices

You can find more information about the tag's advertisement formats following the link:

MikroTik Tag advertisement formats

## Indoor slim rectangular shape - TG-BT5-IN

*[Figure]*

- Temperature range -20..+60°C.
- Built-in accelerometer.
- Magnet activation.
- Dimensions 35x22x7mm.
- BLE 5.2 with Silabs BG22.
- Weatherproof (sealed) version with a built-in non-replaceable LiMnO2 CR2032 (220mAh) battery.

## Overview

TG-BT5-IN is a new addition to our MikroTik equipment. It is a Bluetooth tag (a very small gadget) that can be attached to other equipment or other belonging. Bluetooth tags play a big role in IoT topologies, where Bluetooth is used to broadcast the data over short distances. Once installed and configured, the tag will broadcast advertising packets in iBeacon, Eddystone, or MikroTik telemetry (default packet format) to the gateway (for example, KNOT). Gateway, on the other hand, pushes the advertising packet payload to the remote server utilizing MQTT or HTTP protocols.

## Tag modes

When the product arrives from manufacturing it is set into factory sleep mode. In this mode, all components are shut-down as much as possible and MCU is put into the deepest sleep state. The current draw is reduced to a minimum, so this is the preferred mode to use when the tag is stored and/or not in use. To exit this mode put a magnet to the tag's edge (where the "Magnetic switch" is) and hold it for 3-10 seconds until LED turns off. After that, the tags exits sleep mode and enters advertising mode.

In the Advertising mode, the tag will broadcast Bluetooth advertising packets. By default, MikroTik's advertisement packets are sent once every 5 seconds. This can be changed in the Configuration mode.

Configuration mode can be entered only from advertising mode by applying a magnet to the magnetic switch as in the exiting factory sleep procedure. After applying a magnet for 5-10 seconds LED will turn off and the tag enters configuration mode. If you apply a magnet for longer than 15 seconds or won't connect to the tag with the configuration app, it will go back into advertising mode.

When the device wakes from the factory sleep for the first time, it has this default configuration:

| Configuration parameter | Setting/value |
| --- | --- |
| Advertising packet format | MikroTik |
| Advertising interval | 5.0 seconds |
| Angle Threshold/Tilt trigger | 60° |
| Freefall Threshold/Accelerometer trigger | 156.25 mg |
| Wakeup Threshold/Wakeup trigger | 1.0 mg |
| Bandwith Filter | 0.8 Hz |
| Low noise filter | disabled |
| Tx Power | 0 dBm |

The magnet is used on the reed switch to change the tag's operating modes as described above. As soon as the magnet is detected (the reed switch is activated), the LED will start flashing for the next 5 seconds (first 5 seconds) and, then, stop. It can help you identify that 5 seconds have passed and that you can remove the magnet to enter configuration mode.

*[Figure]*

## Initial steps

Install the "MikroTik Beacon Manager" application and run the app.

For Android devices, you can find it following the link.

- Upon the first login, you will see the list of the nearby devices (devices in either advertising mode or configuration mode):

*[Figure]*

To "wake up" the tag from the factory sleep mode, the reed switch should be activated for 3-10 seconds.

- As soon as the device "wakes up", it will show up in the "MikroTik Beacon Manager" list. Select the tag and you can begin configuring it by pressing the "CONFIG ONLY" button:

*[Figure]*

*[Figure]*

- Right after that, you will need to put a magnet over the device for 10 seconds (this is the step where the device is set to the configuration mode):

*[Figure]*

- After a short wind up time, the device should be ready to be configured:

*[Figure]*

The app will show general information about the tag in the "Status" tab and will allow you to alter the tag's setting using the "Settings" tab (as shown in the screenshot above).

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/tg-bt5-in.md](../regulatory/tg-bt5-in.md).
