# Problems with Netinstall?

> Source: https://help.mikrotik.com/docs/spaces/RKB/pages/1409054/Problems+with+Netinstall
>
> Only on help.mikrotik.com: the manual has no equivalent page. The help site is frozen; this page was last edited 2024-11-07.

## Step 1: Verify Netinstall Setup

1. Test on Another Device: To ensure Netinstall is configured correctly, try Netinstalling a different router.
2. Use the Latest Version: Download the latest Stable or Testing version of Netinstall.
   - [Netinstall tutorial for Windows](https://youtu.be/gzlLbIf3Dbk)
   - [Netinstall tutorial for Linux](https://www.youtube.com/watch?v=CiVwzHwQq_Y)
3. Make sure to access the latest files for this procedure by visiting the products page at <https://mikrotik.com/products> to find your product. The necessary packages can be found under the "Support & Downloads" menu.

## Step 2: Prerequisites for Netinstall

For a successful installation, ensure that your configuration meets these requirements:

- Direct Ethernet Connection: Connect the router’s Ethernet port directly to the PC.
- Same Subnet: Both devices should be on the same subnet.
- Disable Firewalls & Antivirus: Disable any firewall and antivirus programs on your PC.
- Use Reset Button Correctly: Make sure to press the reset button accurately to enable bootp mode.

For more detailed steps, refer to the [MikroTik Netinstall guide](https://help.mikrotik.com/docs/spaces/ROS/pages/24805390/Netinstall).

## Step 3: Using Bootloaders for Netinstall

With Serial Console:

1. Regular Bootloader: Press Ctrl+E in the serial console to enter etherboot mode, or press the Reset button 1-2 seconds after powering on.
2. Backup Bootloader: Power off the device, hold the Reset button, power on the device, wait for the LEDs sequence (blinking, then stable, then off), then release the button.

Without Serial Console:

1. Regular Bootloader: Press the Reset button 1-2 seconds after powering on.
2. Backup Bootloader: Power off the device, hold the Reset button, power on the device, wait for the LEDs sequence (blinking, then stable, then off), then release the button.

## Step 4: Additional Tips

1. Disable Other Network Interfaces: Enable only the interface directly connected to the router for Netinstall.
2. Run as Administrator: Launch netinstall.exe with administrator privileges.
3. For Linux, run  netinstall-cli with sudo.
4. Network Configuration: Set the connection to Private and assign a static IP to the interface.
5. Try Different Ethernet Cables: Replace cables if issues persist.
6. Boot Device Setting: If the router is accessible before reinstalling, go to System > Routerboard > Settings > Boot Device and select "try-ethernet-once-then-nand".

Optional - Use a Switch: In rare cases, placing a switch between the PC and router can resolve hardware compatibility issues. For DHCP snooping, enable "trusted" on bridge ports facing Netinstall.

> **Info**
>
> Optional - Use a Switch: In rare cases, placing a switch between the PC and router can resolve hardware compatibility issues. For DHCP snooping, enable "trusted" on bridge ports facing Netinstall.

> **Info**
>
> Issue: Status shows "ready" without starting the reinstallation after clicking Install.
>
> Solution: Keep the router in bootp mode and restart the Netinstall application. If that doesn’t help, restart your PC and try again.

## Related articles

- [Problems with Netinstall?](https://help.mikrotik.com/docs/spaces/RKB/pages/1409054/Problems+with+Netinstall)
