# PWR-LINE

> Source: https://manual.mikrotik.com/hardware/pwr-line
>
> Category: Data over Powerlines

*[Figure]*

The PWR-LINE series devices allow Ethernet-like connectivity between supported devices over regular electrical power lines. When plugged into the same electrical circuit, the PWR devices will establish Ethernet connectivity by using the HomePlug AV standard.
The PWR-LINE is a smart power adapter with a built-in USB cable.
This particular device is designed for supported MikroTik products with a microUSB port and PWR-LINE support. Connect this adapter to your electrical outlet and then connect the USB cable to power your supported MikroTik device. When doing the same with another PWR-LINE compatible device somewhere further in your premises, the devices will form a connection without needing to install any LAN cables. The device will show up as an additional Ethernet interface in your routers configuration interface. You can install more PWR-LINE devices to further build your network.

## Connecting

- Plug one PWR-LINE device into a power socket.
- Connect the built-in USB cable to the microUSB port of a supported MikroTik router.
- Plug another PWR-LINE unit (or any other compatible device) somewhere in the same electrical circuit. Use the sync button to connect the devices and your local network will automatically be extended. See section Buttons and Jumpers on how to pair additional PWR-LINE devices.

## Powering

The device accepts powering directly from 100-230 V ~50/60Hz wall socket it is plugged into. The power consumption under maximum load can reach 5 W.

## Buttons and jumpers

### PWR connection button (sync)

- Hold 0.5 – 3 seconds. For 120 seconds will try to communicate with another PWR-LINE device. A blinking orange LED light indicates that it is in search mode. You have to also do the same on the other PWR device, so they can synchronize. Press button again to cancel the search.
- Hold 5 – 8 seconds. A new security key is generated. This is needed to remove a PWR-LINE device from an existing PWR network.
- Hold 10 – 15 seconds. Resets all PWR related settings.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/pwr-line.md](../regulatory/pwr-line.md).
