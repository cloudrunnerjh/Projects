
244711424 bytes total (162512896 bytes free)
LBJ-F6IDF-SW2#
*Jun 24 12:06:15.272 CDT: %USBFLASH-5-CHANGE: usbflash0 has been inserted!
LBJ-F6IDF-SW2#
*Jun 24 12:06:19.463 CDT: %USB_HOST_STACK-6-USB_FLASH_READY_TEST_TIME: USB flash 'Ready' test time over 2 seconds.
LBJ-F6IDF-SW2#copy
*Jun 24 12:06:23.558 CDT: %USB_HOST_STACK-6-USB_FLASH_READY_TEST_TIME: USB flash 'Ready' test time over 2 seconds.
LBJ-F6IDF-SW2#copy
*Jun 24 12:06:23.591 CDT: %USBFLASH-4-FORMAT: usbflash0 contains unexpected values in partition table or boot sector.  Device needs formatting before use!
LBJ-F6IDF-SW2#formqusbf
LBJ-F6IDF-SW2#for?
format

LBJ-F6IDF-SW2#form
LBJ-F6IDF-SW2#format usb
LBJ-F6IDF-SW2#format usbflash0:
Format operation may take a while. Continue? [confirm]
Format operation will destroy all data in "usbflash0:".  Continue? [confirm]

*Jun 24 12:07:27.914 CDT: %USB_HOST_STACK-6-USB_FLASH_READY_TEST_TIME: USB flash 'Ready' test time over 2 seconds.

Primary Partition created...Size 668 MB

Drive communication & 1st Sector Write OK...

*Jun 24 12:07:32.033 CDT: %USB_HOST_STACK-6-USB_FLASH_READY_TEST_TIME: USB flash 'Ready' test time over 2 seconds.
*Jun 24 12:07:36.250 CDT: %USB_HOST_STACK-6-USB_FLASH_READY_TEST_TIME: USB flash 'Ready' test time over 2 seconds.
*Jun 24 12:07:40.807 CDT: %USB_HOST_STACK-6-USB_FLASH_READY_TEST_TIME: USB flash 'Ready' test time over 2 seconds.
Format: All system sectors written. OK...

Format: Total sectors in formatted partition: 1368032
Format: Total bytes in formatted partition: 700432384
Format: Operation completed successfully.

Format of usbflash0 complete
LBJ-F6IDF-SW2#
LBJ-F6IDF-SW2#
LBJ-F6IDF-SW2#dir fl
LBJ-F6IDF-SW2#dir flash
%Error opening flash:/flash (No such file or directory)
LBJ-F6IDF-SW2#dir flash:
Directory of flash:/

  772  -rwx        2072  Jun 19 2024 15:17:46 -05:00  multiple-fs
  259  -rwx          35  Mar 28 2024 08:15:30 -05:00  pnp-tech-time
  260  -rwx      106371  Mar 28 2024 08:15:31 -05:00  pnp-tech-discovery-summary
  258  -rwx    38522880  Mar 28 2024 08:20:42 -05:00  c1000-universalk9-tar.152-7.E4.tar
  522  -rwx          52  Mar 28 2024 08:25:28 -05:00  express_setup.debug
  769  drwx        2048  Mar 28 2024 08:27:29 -05:00  pnp-info
 1027  drwx        2048  May 28 2024 10:01:26 -05:00  pnp-tech
  781  drwx        2048  May 28 2024 10:08:27 -05:00  c1000-universalk9-mz.152-7.E10
  527  drwx        2048  May 28 2024 10:08:27 -05:00  dc_profile_dir
  783  -rwx       11699  May 31 2024 11:18:14 -05:00  config.text
  784  -rwx        3566  May 31 2024 11:18:14 -05:00  private-config.text
  261  -rwx         856  Jun 19 2024 15:17:40 -05:00  vlan.dat
    2  drwx        2048  Feb 28 1993 18:00:02 -06:00  lost+found

244711424 bytes total (162512896 bytes free)
LBJ-F6IDF-SW2#dir flash:/c1000-universalk9-mz.152-7.E10
Directory of flash:/c1000-universalk9-mz.152-7.E10/

  272  -rwx         961  May 28 2024 10:04:59 -05:00  info
  275  -rwx    16500736  May 28 2024 10:06:17 -05:00  c1000-universalk9-mz.152-7.E10.bin
  276  drwx        2048  May 28 2024 10:08:26 -05:00  html

244711424 bytes total (162512896 bytes free)
LBJ-F6IDF-SW2#copy flash:/c1000-universalk9-mz.152-7.E10/c1000-universalk9-mz.$
copy flash:/c1000-universalk9-mz.152-7.E10/c1000-universalk9-mz.152-7.E10.bin
% Incomplete command.

LBJ-F6IDF-SW2#$versalk9-mz.152-7.E10/c1000-universalk9-mz.152-7.E10.bin usb
LBJ-F6IDF-SW2#$z.152-7.E10/c1000-universalk9-mz.152-7.E10.bin usbflash0:
Destination filename [c1000-universalk9-mz.152-7.E10.bin]?
Copy in progress...CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
16500736 bytes copied in 18.974 secs (869650 bytes/sec)
LBJ-F6IDF-SW2#dir us
LBJ-F6IDF-SW2#dir usbflash0:
Directory of usbflash0:/

    1  -rw-    16500736  Jun 24 2024 12:09:54 -05:00  c1000-universalk9-mz.152-7.E10.bin

700235776 bytes total (683720704 bytes free)
LBJ-F6IDF-SW2#
*Jun 24 12:10:16.339 CDT: %USBFLASH-5-CHANGE: usbflash0 has been removed!
LBJ-F6IDF-SW2#

switch: dir
USB device descriptor short read (expected 18, got 0)

List of filesystems currently registered:

              xmodem[0]: (read-only)
                null[1]: (read-write)
                vmap[3]: (read-only)
                  bs[4]: (read-only)
                 bsg[5]: (read-only)
               flash[11]: (read-write)


switch: ▒▒▒▒▒H▒蕹▒Ʌ▒▒initialization - Version: 1.0.0
Serdes initialization - Version: 1.0.2
** Link is Gen1, check the EP capability
PEX: pexIdx 0, Link upgraded to Gen2 based on client capabilities
DDR3 Training Sequence - Ver TIP-1.56.0
DDR3 Training Sequence - Switching XBAR Window to FastPath Window
DDR3 Training Sequence - Ended Successfully
BootROM: Image checksum verification PASSED


Board SKU ID is (3)
FPU initialized to Run Fast Mode.
FPGA: 7.0
PCI-e 0: Detected Link.
PCI-e 0: (bus 0) , Detected Link X1, GEN 2.0
DRAM Size: 512 MB
Xmodem file system is available.
USB EHCI 1.00
Using driver version 1 for media type 3
yaffs[10]: Initialization complete.

yaffs[11]: Initialization complete.

yaffs[12]: Initialization complete.

Base ethernet MAC Address: 70:bc:48:71:8f:00
The password-recovery mechanism is enabled.

*** The system will autoboot in 5 seconds ***
Send break character to prevent autobooting.

..................................................
Copying IOS Image from usbflash0:/c1000-universalk9-mz.152-7.E10.bin to flash:/c1000-universalk9-mz.152-7.E10.bin
.............................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................
File "usbflash0:/c1000-universalk9-mz.152-7.E10.bin" successfully copied to "flash:/c1000-universalk9-mz.152-7.E10.bin"
Loading "flash:/c1000-universalk9-mz.152-7.E4/c1000-universalk9-mz.152-7.E4.bin"...
Error loading "flash:/c1000-universalk9-mz.152-7.E4/c1000-universalk9-mz.152-7.E4.bin"

Interrupt within 5 seconds to abort boot process.
..................................................Loading "flash:/c1000-universalk9-mz.152-7.E10.bin"...Verifying image flash:/c1000-universalk9-mz.152-7.E10.bin............................................................................................................................................................................................................................................................
Image passed digital signature verification
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
File "flash:/c1000-universalk9-mz.152-7.E10.bin" uncompressed and installed, entry point: 0x3000
executing...

              Restricted Rights Legend

Use, duplication, or disclosure by the Government is
subject to restrictions as set forth in subparagraph
(c) of the Commercial Computer Software - Restricted
Rights clause at FAR sec. 52.227-19 and subparagraph
(c) (1) (ii) of the Rights in Technical Data and Computer
Software clause at DFARS sec. 252.227-7013.

           cisco Systems, Inc.
           170 West Tasman Drive
           San Jose, California 95134-1706



Cisco IOS Software, C1000 Software (C1000-UNIVERSALK9-M), Version 15.2(7)E10, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2024 by Cisco Systems, Inc.
Compiled Tue 12-Mar-24 08:26 by mcpre
Initializing flash...
Using driver version 1 for media type 3
yaffs[8]: Initialization complete.

yaffs[9]: Initialization complete.

yaffs[10]: Initialization complete.

...done Initializing flash.

Checking for Bootloader upgrade..

Boot Loader upgrade not needed(v)

FIPS: Flash Key Check : Begin
FIPS: Flash Key Check : End, Not Found, FIPS Mode Not Enabled
PCI-e 0: Detected Link.
PCI-e 0: (bus 0) , Detected Link X1, GEN 2.0

MCU version 0x17
Current MCU BL version 0xAE

Checking for MCU firmware upgrade..
 New version = 0x17
 Current version = 0x17

MCU Upgrade not needed!!
INIT: Pp init completed.

INIT: ASIC 0 phases init completed.

INIT: ASIC 1 phases init completed.

INIT: phases init completed.
INIT: features init completed.

POST: PortASIC Port Loopback Tests : Begin
POST: PortASIC Port Loopback Tests : End, Status Passed

POST: ACT2 Authentication : Begin
POST: ACT2 Authentication : End, Status Passed
Waiting for Stack Master Election...
POST: Thermal Tests : Begin
POST: Thermal Tests : End, Status Passed

Election Complete
Switch 1 booting as Master
Initializing Device Manager...
Waiting for Port download...Complete
Resetting PoE Controllers
Initializing OBFL Module......done


This product contains cryptographic features and is subject to United
States and local country laws governing import, export, transfer and
use. Delivery of Cisco cryptographic products does not imply
third-party authority to import, export, distribute or use encryption.
Importers, exporters, distributors and users are responsible for
compliance with U.S. and local country laws. By using this product you
agree to comply with applicable laws and regulations. If you are unable
to comply with U.S. and local laws, return this product immediately.

A summary of U.S. laws governing Cisco cryptographic products may be found at:
http://www.cisco.com/wwl/export/crypto/tool/stqrg.html

If you require further assistance please contact us by sending email to
export@cisco.com.

cisco C1000-48FP-4G-L (Marvell PJ4B (584) v7 (Rev 2)) processor (revision A0) with 524288K bytes of memory.
Processor board ID PSZ28131GWG
Last reset from Reload
1 Virtual Ethernet interface
52 Gigabit Ethernet interfaces
The password-recovery mechanism is enabled.

512K bytes of flash-simulated non-volatile configuration memory.
Base ethernet MAC Address       : 70:BC:48:71:8F:00
Motherboard assembly number     : 69BBA5M1MA02
Power supply part number        : 341-101034-01
Motherboard serial number       : 2452233200160
Power supply serial number      : DCI2809P0AA
Model revision number           : A0
Motherboard revision number     : 2
Model number                    : C1000-48FP-4G-L
Daughterboard assembly number   : 69BBA5Y12A02
Daughterboard serial number     : 2452233300533
System serial number            : PSZ28131GWG
Top Assembly Part Number        : 74-122919-02
Top Assembly Revision Number    : E0
Version ID                      : V02
CLEI Code Number                : CMM5600ARB
Daughterboard revision number   : 2
Hardware Board Revision Number  : 0x01


Switch Ports Model                     SW Version            SW Image
------ ----- -----                     ----------            ----------
*    1 52    C1000-48FP-4G-L           15.2(7)E10            C1000-UNIVERSALK9-M




Press RETURN to get started!


*Mar  1 00:00:01.283:
Board SKU ID is (3)

*Mar  1 00:00:20.257: %STACKMGR-4-SWITCH_ADDED: Switch 1 has been ADDED to the stack
*Mar  1 00:00:23.622: %LINEPROTO-5-UPDOWN: Line protocol on Interface Vlan1, changed state to down
*Jun 24 17:15:53.434: %SPANTREE-5-EXTENDED_SYSID: Extended SysId enabled for type vlan
*Jun 24 17:15:53.960: %PNP-6-PNP_DISCOVERY_STARTED: PnP Discovery started
*Jun 24 17:16:13.201: %USB_HOST_STACK-5-USB_ENUM_FAIL_GETDESCR: Failed to enumerate a USB device as not able to read the device's description.
*Jun 24 11:16:17.000 CST: %SYS-6-CLOCKUPDATE: System clock has been updated from 17:16:17 UTC Mon Jun 24 2024 to 11:16:17 CST Mon Jun 24 2024, configured from console by vty0.
*Jun 24 12:16:17.002 CDT: %SYS-6-CLOCKUPDATE: System clock has been updated from 11:16:17 CST Mon Jun 24 2024 to 12:16:17 CDT Mon Jun 24 2024, configured from console by vty0.
*Jun 24 12:16:17.300 CDT: %LINEPROTO-5-UPDOWN: Line protocol on Interface Vlan20, changed state to down
*Jun 24 12:16:17.365 CDT: %SW_VLAN-6-VTP_DOMAIN_NAME_CHG: VTP domain name changed to NOVTP.
*Jun 24 12:16:17.437 CDT: %SYS-5-CONFIG_I: Configured from memory by console
*Jun 24 12:16:17.770 CDT: %STACKMGR-5-SWITCH_READY: Switch 1 is READY
*Jun 24 12:16:17.770 CDT: %STACKMGR-4-STACK_LINK_CHANGE: Stack Port 1 Switch 1 has changed to state DOWN
*Jun 24 12:16:17.770 CDT: %STACKMGR-4-STACK_LINK_CHANGE: Stack Port 2 Switch 1 has changed to state DOWN
*Jun 24 12:16:18.201 CDT: %STACKMGR-5-MASTER_READY: Master Switch 1 is READY
*Jun 24 12:16:18.356 CDT: %SYS-5-RESTART: System restarted --
Cisco IOS Software, C1000 Software (C1000-UNIVERSALK9-M), Version 15.2(7)E10, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2024 by Cisco Systems, Inc.
Compiled Tue 12-Mar-24 08:26 by mcpre
*Jun 24 12:16:18.451 CDT: %SSH-5-ENABLED: SSH 2.0 has been enabled
*Jun 24 12:16:20.544 CDT: %USB_CONSOLE-6-MEDIA_RJ45: Console media-type is RJ45.
*Jun 24 12:16:23.077 CDT: %LINK-3-UPDOWN: Interface GigabitEthernet1/0/48, changed state to up
*Jun 24 12:16:23.551 CDT: %PNP-6-PNP_BEST_UDI_UPDATE: Best UDI [PID:C1000-48FP-4G-L,VID:V02,SN:PSZ28131GWG] identified via (master-registry)
*Jun 24 12:16:23.551 CDT: %PNP-6-PNP_CDP_UPDATE: Device UDI [PID:C1000-48FP-4G-L,VID:V02,SN:PSZ28131GWG] identified for CDP
*Jun 24 12:16:23.554 CDT: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Startup Config Present)
*Jun 24 12:16:24.357 CDT: %LINEPROTO-5-UPDOWN: Line protocol on Interface Vlan1, changed state to up
*Jun 24 12:16:25.300 CDT: %LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet1/0/48, changed state to up
*Jun 24 12:16:25.781 CDT: %LINEPROTO-5-UPDOWN: Line protocol on Interface Vlan20, changed state to up
***********************************************************
* ACCESS IS RESTRICTED TO AUTHORIZED PERSONNEL ONLY       *
*                                                         *
* Unauthorized access to this system is prohibited and    *
* subject to criminal and civil penalties. Any access or  *
* other connection to this network without the expressed  *
* permission of management is strictly prohibited. All    *
* unauthorized users will be deemed to be trespassing and *
* will be prosecuted to the fullest extent of the law.    *
***********************************************************


User Access Verification

Username: msadmin
Password:

LBJ-F6IDF-SW3#
LBJ-F6IDF-SW3#
LBJ-F6IDF-SW3#sh int ts
LBJ-F6IDF-SW3#sh int st
LBJ-F6IDF-SW3#sh int statu
LBJ-F6IDF-SW3#sh int status

Port      Name               Status       Vlan       Duplex  Speed Type
Gi1/0/1   PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/2   PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/3   PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/4   PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/5   PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/6   PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/7   PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/8   PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/9   PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/10  PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/11  PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX

Port      Name               Status       Vlan       Duplex  Speed Type
Gi1/0/12  PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/13  PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/14  PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/15  PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/16  PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/17  PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/18  PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/19  PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/20  PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/21  PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/22  PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/23  PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX

Port      Name               Status       Vlan       Duplex  Speed Type
Gi1/0/24  PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/25  PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/26  PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/27  PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/28  PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/29  PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/30  PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/31  PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/32  PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/33  PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/34  PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/35  PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX

Port      Name               Status       Vlan       Duplex  Speed Type
Gi1/0/36  PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/37  PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/38  PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/39  PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/40  PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/41  PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/42  PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/43  PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/44  PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/45  PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/46  PC/phone           notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/47  link-to-AL-SW      notconnect   1            auto   auto 10/100/1000BaseTX

Port      Name               Status       Vlan       Duplex  Speed Type
Gi1/0/48  link-to-core       connected    trunk      a-full a-1000 10/100/1000BaseTX
Gi1/0/49  link-to-AL-SW      notconnect   1            auto   auto Not Present
Gi1/0/50  link-to-core       notconnect   1            auto   auto Not Present
Gi1/0/51                     notconnect   1            auto   auto Not Present
Gi1/0/52                     notconnect   1            auto   auto Not Present
LBJ-F6IDF-SW3#
*Jun 24 12:18:49.287 CDT: %USBFLASH-5-CHANGE: usbflash0 has been inserted!
LBJ-F6IDF-SW3#
*Jun 24 12:18:53.346 CDT: %USB_HOST_STACK-6-USB_FLASH_READY_TEST_TIME: USB flash 'Ready' test time over 2 seconds.
LBJ-F6IDF-SW3#
*Jun 24 12:18:57.446 CDT: %USB_HOST_STACK-6-USB_FLASH_READY_TEST_TIME: USB flash 'Ready' test time over 2 seconds.
LBJ-F6IDF-SW3#
LBJ-F6IDF-SW3#dir us
LBJ-F6IDF-SW3#dir usbflash0
%Error opening flash:/usbflash0 (No such file or directory)
LBJ-F6IDF-SW3#dir usbflash0:
Directory of usbflash0:/

    1  -rw-    16500736  Jun 24 2024 12:09:54 -05:00  c1000-universalk9-mz.152-7.E10.bin

700235776 bytes total (683720704 bytes free)
LBJ-F6IDF-SW3#cop
LBJ-F6IDF-SW3#copy usb
LBJ-F6IDF-SW3#copy usbflash0:/c1000-universalk9-mz.152-7.E10.bin fl
LBJ-F6IDF-SW3#copy usbflash0:/c1000-universalk9-mz.152-7.E10.bin flash:
Destination filename [c1000-universalk9-mz.152-7.E10.bin]?
%Warning:There is a file already existing with this name
Do you want to over write? [confirm]^[
LBJ-F6IDF-SW3#dir
Directory of flash:/

  513  -rwx        2072  Jun 24 2024 12:16:23 -05:00  multiple-fs
  259  -rwx          35  Mar 28 2024 08:20:34 -05:00  pnp-tech-time
  260  -rwx      106373  Mar 28 2024 08:20:35 -05:00  pnp-tech-discovery-summary
  258  -rwx    38522880  Mar 28 2024 08:25:47 -05:00  c1000-universalk9-tar.152-7.E4.tar
  521  drwx        2048  Mar 28 2024 08:30:17 -05:00  dc_profile_dir
  779  -rwx          52  Mar 28 2024 08:30:28 -05:00  express_setup.debug
  769  drwx        2048  Mar 28 2024 08:32:28 -05:00  pnp-info
 1027  drwx        2048  May 28 2024 10:19:01 -05:00  pnp-tech
  261  -rwx         856  Jun 24 2024 12:16:17 -05:00  vlan.dat
  264  -rwx       10085  May 31 2024 11:19:18 -05:00  config.text
  265  -rwx        3566  May 31 2024 11:19:18 -05:00  private-config.text
  257  -rwx    16500736  Dec 31 2015 21:25:07 -06:00  c1000-universalk9-mz.152-7.E10.bin
    2  drwx        2048  Feb 28 1993 18:00:02 -06:00  lost+found

244711424 bytes total (185696256 bytes free)
LBJ-F6IDF-SW3#del
LBJ-F6IDF-SW3#delete fl
LBJ-F6IDF-SW3#delete flash:/c1000-universalk9-tar.152-7.E4.tar
Delete filename [c1000-universalk9-tar.152-7.E4.tar]?
Delete flash:/c1000-universalk9-tar.152-7.E4.tar? [confirm]
LBJ-F6IDF-SW3#dir
Directory of flash:/

  513  -rwx        2072  Jun 24 2024 12:16:23 -05:00  multiple-fs
  259  -rwx          35  Mar 28 2024 08:20:34 -05:00  pnp-tech-time
  260  -rwx      106373  Mar 28 2024 08:20:35 -05:00  pnp-tech-discovery-summary
  521  drwx        2048  Mar 28 2024 08:30:17 -05:00  dc_profile_dir
  779  -rwx          52  Mar 28 2024 08:30:28 -05:00  express_setup.debug
  769  drwx        2048  Mar 28 2024 08:32:28 -05:00  pnp-info
 1027  drwx        2048  May 28 2024 10:19:01 -05:00  pnp-tech
  261  -rwx         856  Jun 24 2024 12:16:17 -05:00  vlan.dat
  264  -rwx       10085  May 31 2024 11:19:18 -05:00  config.text
  265  -rwx        3566  May 31 2024 11:19:18 -05:00  private-config.text
  257  -rwx    16500736  Dec 31 2015 21:25:07 -06:00  c1000-universalk9-mz.152-7.E10.bin
    2  drwx        2048  Feb 28 1993 18:00:02 -06:00  lost+found

244711424 bytes total (224221184 bytes free)
LBJ-F6IDF-SW3#
LBJ-F6IDF-SW3#
LBJ-F6IDF-SW3#relo
LBJ-F6IDF-SW3#reload
Proceed with reload? [confirm]
*Jun 24 12:21:57.908 CDT: %USBFLASH-5-CHANGE: usbflash0 has been removed!
[confirm]

*Jun 24 12:22:03.701 CDT: %SYS-5-RELOAD: Reload requested by msadmin on console. Reload Reason: Reload command.▒▒▒▒▒H▒蕹▒Ʌ▒▒initialization - Version: 1.0.0
Serdes initialization - Version: 1.0.2
** Link is Gen1, check the EP capability
PEX: pexIdx 0, Link upgraded to Gen2 based on client capabilities
DDR3 Training Sequence - Ver TIP-1.56.0
DDR3 Training Sequence - Switching XBAR Window to FastPath Window
DDR3 Training Sequence - Ended Successfully
BootROM: Image checksum verification PASSED


Board SKU ID is (3)
FPU initialized to Run Fast Mode.
FPGA: 7.0
PCI-e 0: Detected Link.
PCI-e 0: (bus 0) , Detected Link X1, GEN 2.0
DRAM Size: 512 MB
Xmodem file system is available.
USB EHCI 1.00
Using driver version 1 for media type 3
yaffs[9]: Initialization complete.

yaffs[10]: Initialization complete.

yaffs[11]: Initialization complete.

Base ethernet MAC Address: 70:bc:48:71:8f:00
The password-recovery mechanism is enabled.

*** The system will autoboot in 5 seconds ***
Send break character to prevent autobooting.

..................................................
Loading "flash:/c1000-universalk9-mz.152-7.E4/c1000-universalk9-mz.152-7.E4.bin"...
Error loading "flash:/c1000-universalk9-mz.152-7.E4/c1000-universalk9-mz.152-7.E4.bin"

Interrupt within 5 seconds to abort boot process.
..................................................Loading "flash:/c1000-universalk9-mz.152-7.E10.bin"...Verifying image flash:/c1000-universalk9-mz.152-7.E10.bin............................................................................................................................................................................................................................................................
Image passed digital signature verification
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
File "flash:/c1000-universalk9-mz.152-7.E10.bin" uncompressed and installed, entry point: 0x3000
executing...

              Restricted Rights Legend

Use, duplication, or disclosure by the Government is
subject to restrictions as set forth in subparagraph
(c) of the Commercial Computer Software - Restricted
Rights clause at FAR sec. 52.227-19 and subparagraph
(c) (1) (ii) of the Rights in Technical Data and Computer
Software clause at DFARS sec. 252.227-7013.

           cisco Systems, Inc.
           170 West Tasman Drive
           San Jose, California 95134-1706



Cisco IOS Software, C1000 Software (C1000-UNIVERSALK9-M), Version 15.2(7)E10, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2024 by Cisco Systems, Inc.
Compiled Tue 12-Mar-24 08:26 by mcpre
Initializing flash...
Using driver version 1 for media type 3
yaffs[8]: Initialization complete.

yaffs[9]: Initialization complete.

yaffs[10]: Initialization complete.

...done Initializing flash.

Checking for Bootloader upgrade..

Boot Loader upgrade not needed(v)

FIPS: Flash Key Check : Begin
FIPS: Flash Key Check : End, Not Found, FIPS Mode Not Enabled
PCI-e 0: Detected Link.
PCI-e 0: (bus 0) , Detected Link X1, GEN 2.0

MCU version 0x17
Current MCU BL version 0xAE

Checking for MCU firmware upgrade..
 New version = 0x17
 Current version = 0x17

MCU Upgrade not needed!!
INIT: Pp init completed.

INIT: ASIC 0 phases init completed.

INIT: ASIC 1 phases init completed.

INIT: phases init completed.
INIT: features init completed.

POST: PortASIC Port Loopback Tests : Begin
POST: PortASIC Port Loopback Tests : End, Status Passed

POST: ACT2 Authentication : Begin
POST: ACT2 Authentication : End, Status Passed
Waiting for Stack Master Election...
POST: Thermal Tests : Begin
POST: Thermal Tests : End, Status Passed

Election Complete
Switch 1 booting as Master
Initializing Device Manager...
Waiting for Port download...Complete
Resetting PoE Controllers
Initializing OBFL Module......done


This product contains cryptographic features and is subject to United
States and local country laws governing import, export, transfer and
use. Delivery of Cisco cryptographic products does not imply
third-party authority to import, export, distribute or use encryption.
Importers, exporters, distributors and users are responsible for
compliance with U.S. and local country laws. By using this product you
agree to comply with applicable laws and regulations. If you are unable
to comply with U.S. and local laws, return this product immediately.

A summary of U.S. laws governing Cisco cryptographic products may be found at:
http://www.cisco.com/wwl/export/crypto/tool/stqrg.html

If you require further assistance please contact us by sending email to
export@cisco.com.

cisco C1000-48FP-4G-L (Marvell PJ4B (584) v7 (Rev 2)) processor (revision A0) with 524288K bytes of memory.
Processor board ID PSZ28131GWG
Last reset from Reload
1 Virtual Ethernet interface
52 Gigabit Ethernet interfaces
The password-recovery mechanism is enabled.

512K bytes of flash-simulated non-volatile configuration memory.
Base ethernet MAC Address       : 70:BC:48:71:8F:00
Motherboard assembly number     : 69BBA5M1MA02
Power supply part number        : 341-101034-01
Motherboard serial number       : 2452233200160
Power supply serial number      : DCI2809P0AA
Model revision number           : A0
Motherboard revision number     : 2
Model number                    : C1000-48FP-4G-L
Daughterboard assembly number   : 69BBA5Y12A02
Daughterboard serial number     : 2452233300533
System serial number            : PSZ28131GWG
Top Assembly Part Number        : 74-122919-02
Top Assembly Revision Number    : E0
Version ID                      : V02
CLEI Code Number                : CMM5600ARB
Daughterboard revision number   : 2
Hardware Board Revision Number  : 0x01


Switch Ports Model                     SW Version            SW Image
------ ----- -----                     ----------            ----------
*    1 52    C1000-48FP-4G-L           15.2(7)E10            C1000-UNIVERSALK9-M




Press RETURN to get started!


*Mar  1 00:00:01.283:
Board SKU ID is (3)

*Mar  1 00:00:20.280: %STACKMGR-4-SWITCH_ADDED: Switch 1 has been ADDED to the stack
*Mar  1 00:00:23.644: %LINEPROTO-5-UPDOWN: Line protocol on Interface Vlan1, changed state to down
*Jun 24 17:23:02.439: %SPANTREE-5-EXTENDED_SYSID: Extended SysId enabled for type vlan
*Jun 24 17:23:02.962: %PNP-6-PNP_DISCOVERY_STARTED: PnP Discovery started
*Jun 24 11:23:05.768 CST: %SYS-6-CLOCKUPDATE: System clock has been updated from 17:23:05 UTC Mon Jun 24 2024 to 11:23:05 CST Mon Jun 24 2024, configured from console by vty0.
*Jun 24 12:23:05.769 CDT: %SYS-6-CLOCKUPDATE: System clock has been updated from 11:23:05 CST Mon Jun 24 2024 to 12:23:05 CDT Mon Jun 24 2024, configured from console by vty0.
*Jun 24 12:23:06.065 CDT: %LINEPROTO-5-UPDOWN: Line protocol on Interface Vlan20, changed state to down
*Jun 24 12:23:06.119 CDT: %SW_VLAN-6-VTP_DOMAIN_NAME_CHG: VTP domain name changed to NOVTP.
*Jun 24 12:23:06.170 CDT: %SYS-5-CONFIG_I: Configured from memory by console
*Jun 24 12:23:06.528 CDT: %STACKMGR-5-SWITCH_READY: Switch 1 is READY
*Jun 24 12:23:06.528 CDT: %STACKMGR-4-STACK_LINK_CHANGE: Stack Port 1 Switch 1 has changed to state DOWN
*Jun 24 12:23:06.529 CDT: %STACKMGR-4-STACK_LINK_CHANGE: Stack Port 2 Switch 1 has changed to state DOWN
*Jun 24 12:23:06.952 CDT: %STACKMGR-5-MASTER_READY: Master Switch 1 is READY
*Jun 24 12:23:07.104 CDT: %SYS-5-RESTART: System restarted --
Cisco IOS Software, C1000 Software (C1000-UNIVERSALK9-M), Version 15.2(7)E10, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2024 by Cisco Systems, Inc.
Compiled Tue 12-Mar-24 08:26 by mcpre
*Jun 24 12:23:07.199 CDT: %SSH-5-ENABLED: SSH 2.0 has been enabled
*Jun 24 12:23:09.541 CDT: %USB_CONSOLE-6-MEDIA_RJ45: Console media-type is RJ45.
*Jun 24 12:23:11.906 CDT: %LINK-3-UPDOWN: Interface GigabitEthernet1/0/48, changed state to up
*Jun 24 12:23:12.260 CDT: %PNP-6-PNP_BEST_UDI_UPDATE: Best UDI [PID:C1000-48FP-4G-L,VID:V02,SN:PSZ28131GWG] identified via (master-registry)
*Jun 24 12:23:12.260 CDT: %PNP-6-PNP_CDP_UPDATE: Device UDI [PID:C1000-48FP-4G-L,VID:V02,SN:PSZ28131GWG] identified for CDP
*Jun 24 12:23:12.262 CDT: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Startup Config Present)
*Jun 24 12:23:13.161 CDT: %LINEPROTO-5-UPDOWN: Line protocol on Interface Vlan1, changed state to up
*Jun 24 12:23:13.161 CDT: %LINEPROTO-5-UPDOWN: Line protocol on Interface Vlan20, changed state to up
*Jun 24 12:23:14.130 CDT: %LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet1/0/48, changed state to up
***********************************************************
* ACCESS IS RESTRICTED TO AUTHORIZED PERSONNEL ONLY       *
*                                                         *
* Unauthorized access to this system is prohibited and    *
* subject to criminal and civil penalties. Any access or  *
* other connection to this network without the expressed  *
* permission of management is strictly prohibited. All    *
* unauthorized users will be deemed to be trespassing and *
* will be prosecuted to the fullest extent of the law.    *
***********************************************************


User Access Verification

Username: msadmin
Password:

LBJ-F6IDF-SW3#sh cdp nei
LBJ-F6IDF-SW3#sh cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone,
                  D - Remote, C - CVTA, M - Two-port Mac Relay

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
LBJ-COR-SW1.randa.com
                 Gig 1/0/48        155             R S I  C9300-48P Gig 1/0/47

Total cdp entries displayed : 1
LBJ-F6IDF-SW3#
LBJ-F6IDF-SW3#
LBJ-F6IDF-SW3#
LBJ-F6IDF-SW3#
LBJ-F6IDF-SW3#▒▒▒▒▒H▒蕹▒Ʌ▒▒initialization - Version: 1.0.0
Serdes initialization - Version: 1.0.2
** Link is Gen1, check the EP capability
PEX: pexIdx 0, Link upgraded to Gen2 based on client capabilities
DDR3 Training Sequence - Ver TIP-1.56.0
DDR3 Training Sequence - Switching XBAR Window to FastPath Window
DDR3 Training Sequence - Ended Successfully
BootROM: Image checksum verification PASSED


Board SKU ID is (3)
FPU initialized to Run Fast Mode.
FPGA: 7.0
PCI-e 0: Detected Link.
PCI-e 0: (bus 0) , Detected Link X1, GEN 2.0
DRAM Size: 512 MB
Xmodem file system is available.
USB EHCI 1.00
Using driver version 1 for media type 3
yaffs[9]: Initialization complete.

yaffs[10]: Initialization complete.

yaffs[11]: Initialization complete.

Base ethernet MAC Address: 70:bc:48:71:8f:00
The password-recovery mechanism is enabled.

*** The system will autoboot in 5 seconds ***
Send break character to prevent autobooting.

..................................................
Loading "flash:/c1000-universalk9-mz.152-7.E4/c1000-universalk9-mz.152-7.E4.bin"...
Error loading "flash:/c1000-universalk9-mz.152-7.E4/c1000-universalk9-mz.152-7.E4.bin"

Interrupt within 5 seconds to abort boot process.
..................................................Loading "flash:/c1000-universalk9-mz.152-7.E10.bin"...Verifying image flash:/c1000-universalk9-mz.152-7.E10.bin............................................................................................................................................................................................................................................................
Image passed digital signature verification
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
File "flash:/c1000-universalk9-mz.152-7.E10.bin" uncompressed and installed, entry point: 0x3000
executing...

              Restricted Rights Legend

Use, duplication, or disclosure by the Government is
subject to restrictions as set forth in subparagraph
(c) of the Commercial Computer Software - Restricted
Rights clause at FAR sec. 52.227-19 and subparagraph
(c) (1) (ii) of the Rights in Technical Data and Computer
Software clause at DFARS sec. 252.227-7013.

           cisco Systems, Inc.
           170 West Tasman Drive
           San Jose, California 95134-1706



Cisco IOS Software, C1000 Software (C1000-UNIVERSALK9-M), Version 15.2(7)E10, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2024 by Cisco Systems, Inc.
Compiled Tue 12-Mar-24 08:26 by mcpre
Initializing flash...
Using driver version 1 for media type 3
yaffs[8]: Initialization complete.

yaffs[9]: Initialization complete.

yaffs[10]: Initialization complete.

...done Initializing flash.

Checking for Bootloader upgrade..

Boot Loader upgrade not needed(v)

FIPS: Flash Key Check : Begin
FIPS: Flash Key Check : End, Not Found, FIPS Mode Not Enabled
PCI-e 0: Detected Link.
PCI-e 0: (bus 0) , Detected Link X1, GEN 2.0

MCU version 0x17
Current MCU BL version 0xAE

Checking for MCU firmware upgrade..
 New version = 0x17
 Current version = 0x17

MCU Upgrade not needed!!
INIT: Pp init completed.

INIT: ASIC 0 phases init completed.

INIT: ASIC 1 phases init completed.

INIT: phases init completed.
INIT: features init completed.

POST: PortASIC Port Loopback Tests : Begin
POST: PortASIC Port Loopback Tests : End, Status Passed

POST: ACT2 Authentication : Begin
POST: ACT2 Authentication : End, Status Passed
Waiting for Stack Master Election...
POST: Thermal Tests : Begin
POST: Thermal Tests : End, Status Passed

Election Complete
Switch 1 booting as Master
Initializing Device Manager...
Waiting for Port download...Complete
Resetting PoE Controllers
Initializing OBFL Module......done


This product contains cryptographic features and is subject to United
States and local country laws governing import, export, transfer and
use. Delivery of Cisco cryptographic products does not imply
third-party authority to import, export, distribute or use encryption.
Importers, exporters, distributors and users are responsible for
compliance with U.S. and local country laws. By using this product you
agree to comply with applicable laws and regulations. If you are unable
to comply with U.S. and local laws, return this product immediately.

A summary of U.S. laws governing Cisco cryptographic products may be found at:
http://www.cisco.com/wwl/export/crypto/tool/stqrg.html

If you require further assistance please contact us by sending email to
export@cisco.com.

cisco C1000-48FP-4G-L (Marvell PJ4B (584) v7 (Rev 2)) processor (revision A0) with 524288K bytes of memory.
Processor board ID PSZ28131GWG
Last reset from Reload
1 Virtual Ethernet interface
52 Gigabit Ethernet interfaces
The password-recovery mechanism is enabled.

512K bytes of flash-simulated non-volatile configuration memory.
Base ethernet MAC Address       : 70:BC:48:71:8F:00
Motherboard assembly number     : 69BBA5M1MA02
Power supply part number        : 341-101034-01
Motherboard serial number       : 2452233200160
Power supply serial number      : DCI2809P0AA
Model revision number           : A0
Motherboard revision number     : 2
Model number                    : C1000-48FP-4G-L
Daughterboard assembly number   : 69BBA5Y12A02
Daughterboard serial number     : 2452233300533
System serial number            : PSZ28131GWG
Top Assembly Part Number        : 74-122919-02
Top Assembly Revision Number    : E0
Version ID                      : V02
CLEI Code Number                : CMM5600ARB
Daughterboard revision number   : 2
Hardware Board Revision Number  : 0x01


Switch Ports Model                     SW Version            SW Image
------ ----- -----                     ----------            ----------
*    1 52    C1000-48FP-4G-L           15.2(7)E10            C1000-UNIVERSALK9-M




Press RETURN to get started!


*Mar  1 00:00:01.283:
Board SKU ID is (3)

*Mar  1 00:00:20.238: %STACKMGR-4-SWITCH_ADDED: Switch 1 has been ADDED to the stack
*Mar  1 00:00:23.604: %LINEPROTO-5-UPDOWN: Line protocol on Interface Vlan1, changed state to down
*Jun 24 17:26:27.439: %SPANTREE-5-EXTENDED_SYSID: Extended SysId enabled for type vlan
*Jun 24 17:26:27.962: %PNP-6-PNP_DISCOVERY_STARTED: PnP Discovery started
*Jun 24 11:26:30.773 CST: %SYS-6-CLOCKUPDATE: System clock has been updated from 17:26:30 UTC Mon Jun 24 2024 to 11:26:30 CST Mon Jun 24 2024, configured from console by vty0.
*Jun 24 12:26:30.774 CDT: %SYS-6-CLOCKUPDATE: System clock has been updated from 11:26:30 CST Mon Jun 24 2024 to 12:26:30 CDT Mon Jun 24 2024, configured from console by vty0.
*Jun 24 12:26:31.068 CDT: %LINEPROTO-5-UPDOWN: Line protocol on Interface Vlan20, changed state to down
*Jun 24 12:26:31.134 CDT: %SW_VLAN-6-VTP_DOMAIN_NAME_CHG: VTP domain name changed to NOVTP.
*Jun 24 12:26:31.206 CDT: %SYS-5-CONFIG_I: Configured from memory by console
*Jun 24 12:26:31.564 CDT: %STACKMGR-5-SWITCH_READY: Switch 1 is READY
*Jun 24 12:26:31.564 CDT: %STACKMGR-4-STACK_LINK_CHANGE: Stack Port 1 Switch 1 has changed to state DOWN
*Jun 24 12:26:31.564 CDT: %STACKMGR-4-STACK_LINK_CHANGE: Stack Port 2 Switch 1 has changed to state DOWN
*Jun 24 12:26:31.987 CDT: %STACKMGR-5-MASTER_READY: Master Switch 1 is READY
*Jun 24 12:26:32.139 CDT: %SYS-5-RESTART: System restarted --
Cisco IOS Software, C1000 Software (C1000-UNIVERSALK9-M), Version 15.2(7)E10, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2024 by Cisco Systems, Inc.
Compiled Tue 12-Mar-24 08:26 by mcpre
*Jun 24 12:26:32.234 CDT: %SSH-5-ENABLED: SSH 2.0 has been enabled
*Jun 24 12:26:34.581 CDT: %USB_CONSOLE-6-MEDIA_RJ45: Console media-type is RJ45.
*Jun 24 12:26:36.941 CDT: %LINK-3-UPDOWN: Interface GigabitEthernet1/0/48, changed state to up
*Jun 24 12:26:37.302 CDT: %PNP-6-PNP_BEST_UDI_UPDATE: Best UDI [PID:C1000-48FP-4G-L,VID:V02,SN:PSZ28131GWG] identified via (master-registry)
*Jun 24 12:26:37.302 CDT: %PNP-6-PNP_CDP_UPDATE: Device UDI [PID:C1000-48FP-4G-L,VID:V02,SN:PSZ28131GWG] identified for CDP
*Jun 24 12:26:37.304 CDT: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Startup Config Present)
*Jun 24 12:26:38.194 CDT: %LINEPROTO-5-UPDOWN: Line protocol on Interface Vlan1, changed state to up
*Jun 24 12:26:38.445 CDT: %LINEPROTO-5-UPDOWN: Line protocol on Interface Vlan20, changed state to up
*Jun 24 12:26:39.164 CDT: %LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet1/0/48, changed state to up
***********************************************************
* ACCESS IS RESTRICTED TO AUTHORIZED PERSONNEL ONLY       *
*                                                         *
* Unauthorized access to this system is prohibited and    *
* subject to criminal and civil penalties. Any access or  *
* other connection to this network without the expressed  *
* permission of management is strictly prohibited. All    *
* unauthorized users will be deemed to be trespassing and *
* will be prosecuted to the fullest extent of the law.    *
***********************************************************


User Access Verification

Username: msadmin
Password:

LBJ-F6IDF-SW3#dir
Directory of flash:/

  258  -rwx        2072  Jun 24 2024 12:26:37 -05:00  multiple-fs
  259  -rwx          35  Mar 28 2024 08:20:34 -05:00  pnp-tech-time
  260  -rwx      106373  Mar 28 2024 08:20:35 -05:00  pnp-tech-discovery-summary
  521  drwx        2048  Mar 28 2024 08:30:17 -05:00  dc_profile_dir
  779  -rwx          52  Mar 28 2024 08:30:28 -05:00  express_setup.debug
  769  drwx        2048  Mar 28 2024 08:32:28 -05:00  pnp-info
 1027  drwx        2048  May 28 2024 10:19:01 -05:00  pnp-tech
  264  -rwx       10085  May 31 2024 11:19:18 -05:00  config.text
  265  -rwx        3566  May 31 2024 11:19:18 -05:00  private-config.text
  257  -rwx    16500736  Dec 31 2015 21:25:07 -06:00  c1000-universalk9-mz.152-7.E10.bin
  261  -rwx         856  Jun 24 2024 12:26:31 -05:00  vlan.dat
    2  drwx        2048  Feb 28 1993 18:00:02 -06:00  lost+found

244711424 bytes total (224221184 bytes free)
LBJ-F6IDF-SW3#sh run
Building configuration...

Current configuration : 10074 bytes
!
! Last configuration change at 12:26:41 CDT Mon Jun 24 2024
!
version 15.2
no service pad
service timestamps debug datetime msec localtime show-timezone
service timestamps log datetime msec localtime show-timezone
service password-encryption
!
hostname LBJ-F6IDF-SW3
!
boot-start-marker
boot-end-marker
!
!
username msadmin privilege 15 secret 9 $9$DjVhwle.HF4/VL$zaEOORK8hXOZQAaUYqfZ57ihOCufAtCi464Gy7y1dgM
username jwilliams privilege 15 secret 9 $9$wodkxOItmS964k$GOlKUhRA.af/hUfqs/j3F8nDg/Zj0SAqHFSl0dbutoo
aaa new-model
!
!
aaa authentication login default local
!
!
!
!
!
!
aaa session-id common
clock timezone CST -6 0
clock summer-time CDT recurring
switch 1 provision c1000-48fp-4g-l
system mtu routing 1500
!
!
ip domain-name randa.com
vtp domain NOVTP
vtp mode transparent
!
!
!
!
!
!
!
!
spanning-tree mode rapid-pvst
spanning-tree portfast edge bpduguard default
spanning-tree extend system-id
!
vlan internal allocation policy ascending
!
vlan 4
 name users
!
vlan 6
 name server
!
vlan 8
 name voice
!
vlan 20
 name NW-mgmt
!
vlan 220
 name camera

LBJ-F6IDF-SW3#
LBJ-F6IDF-SW3#sh ip int br
Interface              IP-Address      OK? Method Status                Protocol
Vlan1                  unassigned      YES NVRAM  up                    up
Vlan20                 10.202.20.13    YES NVRAM  up                    up
GigabitEthernet1/0/1   unassigned      YES unset  down                  down
GigabitEthernet1/0/2   unassigned      YES unset  down                  down
GigabitEthernet1/0/3   unassigned      YES unset  down                  down
GigabitEthernet1/0/4   unassigned      YES unset  down                  down
GigabitEthernet1/0/5   unassigned      YES unset  down                  down
GigabitEthernet1/0/6   unassigned      YES unset  down                  down
GigabitEthernet1/0/7   unassigned      YES unset  down                  down
GigabitEthernet1/0/8   unassigned      YES unset  down                  down
GigabitEthernet1/0/9   unassigned      YES unset  down                  down
GigabitEthernet1/0/10  unassigned      YES unset  down                  down
GigabitEthernet1/0/11  unassigned      YES unset  down                  down
GigabitEthernet1/0/12  unassigned      YES unset  down                  down
GigabitEthernet1/0/13  unassigned      YES unset  down                  down
GigabitEthernet1/0/14  unassigned      YES unset  down                  down
GigabitEthernet1/0/15  unassigned      YES unset  down                  down
GigabitEthernet1/0/16  unassigned      YES unset  down                  down
GigabitEthernet1/0/17  unassigned      YES unset  down                  down
GigabitEthernet1/0/18  unassigned      YES unset  down                  down
GigabitEthernet1/0/19  unassigned      YES unset  down                  down

LBJ-F6IDF-SW3#ping 4.2.2.2
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 4.2.2.2, timeout is 2 seconds:
.....
Success rate is 0 percent (0/5)
LBJ-F6IDF-SW3#ssh 10.202.20.1
Password:

***********************************************************
* ACCESS IS RESTRICTED TO AUTHORIZED PERSONNEL ONLY       *
*                                                         *
* Unauthorized access to this system is prohibited and    *
* subject to criminal and civil penalties. Any access or  *
* other connection to this network without the expressed  *
* permission of management is strictly prohibited. All    *
* unauthorized users will be deemed to be trespassing and *
* will be prosecuted to the fullest extent of the law.    *
***********************************************************



LBJ-COR-SW1#
LBJ-COR-SW1#sh cdp nei
LBJ-COR-SW1#sh cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone,
                  D - Remote, C - CVTA, M - Two-port Mac Relay

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
LBJ-F6IDF-SW2.randa.com
                 Gig 1/0/46        137              S I   C1000-48F Gig 1/0/48
LBJ-F6IDF-SW3.randa.com
                 Gig 1/0/47        169              S I   C1000-48F Gig 1/0/48
LBJ-F6IDF-SW1.randa.com
                 Gig 1/0/45        132              S I   C1000-48F Gig 1/0/48
LBJ-F6IDF-SW4.randa.com
                 Gig 1/0/48        142              S I   C1000-48F Gig 1/0/48
LBJ-F2IDF-SW1.randa.com
                 Ten 1/1/3         149              S I   C1000-48F Gig 1/0/50
LBJ-F2IDF-SW1.randa.com
                 Ten 1/1/4         168              S I   C1000-48F Gig 1/0/49

Total cdp entries displayed : 6
LBJ-COR-SW1#
LBJ-COR-SW1#ping 4.2.2.2
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 4.2.2.2, timeout is 2 seconds:
.....
Success rate is 0 percent (0/5)
LBJ-COR-SW1#sh lldp nei
LBJ-COR-SW1#sh lldp neighbors
% LLDP is not enabled
LBJ-COR-SW1#lld
LBJ-COR-SW1#lld?
% Unrecognized command
LBJ-COR-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
LBJ-COR-SW1(config)#lldp en
LBJ-COR-SW1(config)#lldp ?
  custom-network-hash  Custom Network Hash
  holdtime             Specify the holdtime (in sec) to be sent in packets
  management-address   Management IP
  management-vlan      Management Vlan Id
  reinit               Delay (in sec) for LLDP initialization on any interface
  run                  Enable LLDP
  system-name          System Name
  timer                Specify the rate at which LLDP packets are sent (in sec)
  tlv-select           Selection of LLDP TLVs to send
  ucs-tlv              Selection of UCS LLDP TLVs to send

LBJ-COR-SW1(config)#lldp run
LBJ-COR-SW1(config)#^Z
LBJ-COR-SW1#wr
Building configuration...
[OK]
LBJ-COR-SW1#sho lldp nei
LBJ-COR-SW1#sho lldp neighbors
Capability codes:
    (R) Router, (B) Bridge, (T) Telephone, (C) DOCSIS Cable Device
    (W) WLAN Access Point, (P) Repeater, (S) Station, (O) Other

Device ID           Local Intf     Hold-time  Capability      Port ID
cida341-lbj-fw1     Gi1/0/38       120        R               port5

Total entries displayed: 1

LBJ-COR-SW1#sh lld
LBJ-COR-SW1#sh lldp en
LBJ-COR-SW1#sh lldp entry cida341-lbj-fw1

Capability codes:
    (R) Router, (B) Bridge, (T) Telephone, (C) DOCSIS Cable Device
    (W) WLAN Access Point, (P) Repeater, (S) Station, (O) Other
------------------------------------------------
Local Intf: Gi1/0/38
Chassis id: 8439.8faa.000c
Port id: port5
Port Description - not advertised
System Name: cida341-lbj-fw1

System Description:
FortiGate-100F v7.0.14,build0601,240206 (GA.M)

Time remaining: 93 seconds
System Capabilities: B,R
Enabled Capabilities: R
Management Addresses - not advertised
Auto Negotiation - not supported
Physical media capabilities - not advertised
Media Attachment Unit type - not advertised
Vlan ID: - not advertised
Peer Source MAC: 8439.8faa.0016


Total entries displayed: 1
LBJ-COR-SW1#sh ip rou
LBJ-COR-SW1#sh ip route
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, m - OMP
       n - NAT, Ni - NAT inside, No - NAT outside, Nd - NAT DIA
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       H - NHRP, G - NHRP registered, g - NHRP registration summary
       o - ODR, P - periodic downloaded static route, l - LISP
       a - application route
       + - replicated route, % - next hop override, p - overrides from PfR
       & - replicated local route overrides by connected

Gateway of last resort is not set

      10.0.0.0/8 is variably subnetted, 12 subnets, 2 masks
C        10.202.4.0/24 is directly connected, Vlan4
L        10.202.4.1/32 is directly connected, Vlan4
C        10.202.6.0/24 is directly connected, Vlan6
L        10.202.6.1/32 is directly connected, Vlan6
C        10.202.8.0/24 is directly connected, Vlan8
L        10.202.8.1/32 is directly connected, Vlan8
C        10.202.20.0/24 is directly connected, Vlan20
L        10.202.20.1/32 is directly connected, Vlan20
C        10.202.30.0/24 is directly connected, Vlan30
L        10.202.30.1/32 is directly connected, Vlan30
C        10.202.220.0/24 is directly connected, Vlan220
L        10.202.220.1/32 is directly connected, Vlan220
LBJ-COR-SW1# sh vl
LBJ-COR-SW1# sh vlan

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Gi1/0/3, Gi1/0/4, Gi1/0/5
                                                Gi1/0/6, Gi1/0/7, Gi1/0/8
                                                Gi1/0/9, Gi1/0/10, Gi1/0/11
                                                Gi1/0/12, Gi1/0/13, Gi1/0/14
                                                Gi1/0/15, Gi1/0/16, Gi1/0/17
                                                Gi1/0/18, Gi1/0/19, Gi1/0/20
                                                Gi1/0/21, Gi1/0/22, Gi1/0/23
                                                Gi1/0/24, Gi1/0/25, Gi1/0/26
                                                Gi1/0/27, Gi1/0/28, Gi1/0/29
                                                Gi1/0/30, Gi1/0/31, Gi1/0/32
                                                Gi1/0/33, Gi1/0/34, Gi1/0/35
                                                Gi1/0/36, Gi1/0/39, Gi1/0/40
                                                Gi1/0/41, Gi1/0/42, Gi1/0/43
                                                Gi1/0/44, Te1/1/1, Te1/1/2
                                                Te1/1/5, Te1/1/6, Te1/1/7
                                                Te1/1/8, Ap1/0/1
4    users                            active    Gi1/0/1, Gi1/0/2
6    Server-Mgmt                      active
8    voice                            active
20   NW-mgmt                          active    Gi1/0/37, Gi1/0/38

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
30   transit                          active
220  Cameras                          active
1002 fddi-default                     act/unsup
1003 token-ring-default               act/unsup
1004 fddinet-default                  act/unsup
1005 trnet-default                    act/unsup

VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
1    enet  100001     1500  -      -      -        -    -        0      0
4    enet  100004     1500  -      -      -        -    -        0      0
6    enet  100006     1500  -      -      -        -    -        0      0
8    enet  100008     1500  -      -      -        -    -        0      0
20   enet  100020     1500  -      -      -        -    -        0      0
30   enet  100030     1500  -      -      -        -    -        0      0
220  enet  100220     1500  -      -      -        -    -        0      0
1002 fddi  101002     1500  -      -      -        -    -        0      0
1003 tr    101003     1500  -      -      -        -    -        0      0
1004 fdnet 101004     1500  -      -      -        ieee -        0      0
1005 trnet 101005     1500  -      -      -        ibm  -        0      0

Remote SPAN VLANs
------------------------------------------------------------------------------

LBJ-COR-SW1#h ip int br
help ip int br
     ^
% Invalid input detected at '^' marker.

LBJ-COR-SW1#sh ip int br
Interface              IP-Address      OK? Method Status                Protocol
Vlan1                  unassigned      YES NVRAM  up                    up
Vlan4                  10.202.4.1      YES NVRAM  up                    up
Vlan6                  10.202.6.1      YES NVRAM  up                    up
Vlan8                  10.202.8.1      YES NVRAM  up                    up
Vlan20                 10.202.20.1     YES NVRAM  up                    up
Vlan30                 10.202.30.1     YES NVRAM  up                    up
Vlan220                10.202.220.1    YES NVRAM  up                    up
GigabitEthernet0/0     unassigned      YES NVRAM  administratively down down
GigabitEthernet1/0/1   unassigned      YES unset  down                  down
GigabitEthernet1/0/2   unassigned      YES unset  down                  down
GigabitEthernet1/0/3   unassigned      YES unset  down                  down
GigabitEthernet1/0/4   unassigned      YES unset  down                  down
GigabitEthernet1/0/5   unassigned      YES unset  down                  down
GigabitEthernet1/0/6   unassigned      YES unset  down                  down
GigabitEthernet1/0/7   unassigned      YES unset  down                  down
GigabitEthernet1/0/8   unassigned      YES unset  down                  down
GigabitEthernet1/0/9   unassigned      YES unset  down                  down
GigabitEthernet1/0/10  unassigned      YES unset  down                  down
GigabitEthernet1/0/11  unassigned      YES unset  down                  down
GigabitEthernet1/0/12  unassigned      YES unset  down                  down
GigabitEthernet1/0/13  unassigned      YES unset  down                  down
GigabitEthernet1/0/14  unassigned      YES unset  down                  down

LBJ-COR-SW1#sh ip rou
LBJ-COR-SW1#sh ip route
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, m - OMP
       n - NAT, Ni - NAT inside, No - NAT outside, Nd - NAT DIA
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       H - NHRP, G - NHRP registered, g - NHRP registration summary
       o - ODR, P - periodic downloaded static route, l - LISP
       a - application route
       + - replicated route, % - next hop override, p - overrides from PfR
       & - replicated local route overrides by connected

Gateway of last resort is not set

      10.0.0.0/8 is variably subnetted, 12 subnets, 2 masks
C        10.202.4.0/24 is directly connected, Vlan4
L        10.202.4.1/32 is directly connected, Vlan4
C        10.202.6.0/24 is directly connected, Vlan6
L        10.202.6.1/32 is directly connected, Vlan6
C        10.202.8.0/24 is directly connected, Vlan8
L        10.202.8.1/32 is directly connected, Vlan8
C        10.202.20.0/24 is directly connected, Vlan20
L        10.202.20.1/32 is directly connected, Vlan20
C        10.202.30.0/24 is directly connected, Vlan30
L        10.202.30.1/32 is directly connected, Vlan30
C        10.202.220.0/24 is directly connected, Vlan220
L        10.202.220.1/32 is directly connected, Vlan220
LBJ-COR-SW1#ping 10.202.30.5
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.202.30.5, timeout is 2 seconds:
.....
Success rate is 0 percent (0/5)
LBJ-COR-SW1#sh run | sec route
ip route 0.0.0.0 0.0.0.0 10.202.50.2
LBJ-COR-SW1#sh run
Building configuration...

Current configuration : 13440 bytes
!
! Last configuration change at 12:22:53 CDT Mon Jun 24 2024 by msadmin
!
version 17.9
service timestamps debug datetime msec localtime show-timezone
service timestamps log datetime msec localtime show-timezone
service password-encryption
service call-home
platform punt-keepalive disable-kernel-core
!
hostname LBJ-COR-SW1
!
!
vrf definition Mgmt-vrf
 !
 address-family ipv4
 exit-address-family
 !
 address-family ipv6
 exit-address-family
!
aaa new-model
!
!
aaa authentication login default local
!
!
aaa session-id common
clock timezone CST -6 0
clock summer-time CDT recurring
switch 1 provision c9300-48p
!
!
!
!
ip routing
!
!
!
!
!
ip domain name randa.com
!
!
!
login on-success log
vtp domain NOVTP
vtp mode transparent
vtp version 1
!
!
!
!
!
!
!
!
!
crypto pki trustpoint SLA-TrustPoint
 enrollment pkcs12
 revocation-check crl
!
crypto pki trustpoint TP-self-signed-3765994784
 enrollment selfsigned
 subject-name cn=IOS-Self-Signed-Certificate-3765994784
 revocation-check none
 rsakeypair TP-self-signed-3765994784
!
!
crypto pki certificate chain SLA-TrustPoint
 certificate ca 01
  30820321 30820209 A0030201 02020101 300D0609 2A864886 F70D0101 0B050030
  32310E30 0C060355 040A1305 43697363 6F312030 1E060355 04031317 43697363
  6F204C69 63656E73 696E6720 526F6F74 20434130 1E170D31 33303533 30313934
  3834375A 170D3338 30353330 31393438 34375A30 32310E30 0C060355 040A1305
  43697363 6F312030 1E060355 04031317 43697363 6F204C69 63656E73 696E6720
  526F6F74 20434130 82012230 0D06092A 864886F7 0D010101 05000382 010F0030
  82010A02 82010100 A6BCBD96 131E05F7 145EA72C 2CD686E6 17222EA1 F1EFF64D
  CBB4C798 212AA147 C655D8D7 9471380D 8711441E 1AAF071A 9CAE6388 8A38E520
  1C394D78 462EF239 C659F715 B98C0A59 5BBB5CBD 0CFEBEA3 700A8BF7 D8F256EE
  4AA4E80D DB6FD1C9 60B1FD18 FFC69C96 6FA68957 A2617DE7 104FDC5F EA2956AC
  7390A3EB 2B5436AD C847A2C5 DAB553EB 69A9A535 58E9F3E3 C0BD23CF 58BD7188
  68E69491 20F320E7 948E71D7 AE3BCC84 F10684C7 4BC8E00F 539BA42B 42C68BB7
  C7479096 B4CB2D62 EA2F505D C7B062A4 6811D95B E8250FC4 5D5D5FB8 8F27D191
  C55F0D76 61F9A4CD 3D992327 A8BB03BD 4E6D7069 7CBADF8B DF5F4368 95135E44
  DFC7C6CF 04DD7FD1 02030100 01A34230 40300E06 03551D0F 0101FF04 04030201
  06300F06 03551D13 0101FF04 05300301 01FF301D 0603551D 0E041604 1449DC85
  4B3D31E5 1B3E6A17 606AF333 3D3B4C73 E8300D06 092A8648 86F70D01 010B0500
  03820101 00507F24 D3932A66 86025D9F E838AE5C 6D4DF6B0 49631C78 240DA905
  604EDCDE FF4FED2B 77FC460E CD636FDB DD44681E 3A5673AB 9093D3B1 6C9E3D8B
  D98987BF E40CBD9E 1AECA0C2 2189BB5C 8FA85686 CD98B646 5575B146 8DFC66A8
  467A3DF4 4D565700 6ADF0F0D CF835015 3C04FF7C 21E878AC 11BA9CD2 55A9232C
  7CA7B7E6 C1AF74F6 152E99B7 B1FCF9BB E973DE7F 5BDDEB86 C71E3B49 1765308B
  5FB0DA06 B92AFE7F 494E8A9E 07B85737 F3A58BE1 1A48A229 C37C1E69 39F08678
  80DDCD16 D6BACECA EEBC7CF9 8428787B 35202CDC 60E4616A B623CDBD 230E3AFB
  418616A9 4093E049 4D10AB75 27E86F73 932E35B5 8862FDAE 0275156F 719BB2F0
  D697DF7F 28
        quit
crypto pki certificate chain TP-self-signed-3765994784
 certificate self-signed 01
  30820330 30820218 A0030201 02020101 300D0609 2A864886 F70D0101 05050030
  31312F30 2D060355 04031326 494F532D 53656C66 2D536967 6E65642D 43657274
  69666963 6174652D 33373635 39393437 3834301E 170D3234 30353234 31383335
  34345A17 0D333430 35323431 38333534 345A3031 312F302D 06035504 03132649
  4F532D53 656C662D 5369676E 65642D43 65727469 66696361 74652D33 37363539
  39343738 34308201 22300D06 092A8648 86F70D01 01010500 0382010F 00308201
  0A028201 0100DC9D 9E1C65C6 F64B3EE4 87FE0187 AA3AA69A 76938904 C989EAAE
  56C422A6 E7CBC78F F07BEFCC 0818671B D7DD46D2 C3C57F88 BC98B7EF B409B77F
  004C6B1D 59E06420 D03626D2 78EFE125 B8DF1F8D 8F373361 D9342D38 60D13ACC
  EE746DDA 2BA6130B 6D7A1AFB F9AD3F54 7826267E 0610254F 92613A11 E4BC36F0
  DD699788 2FB57E52 965EBA88 A6415F9B E956BC11 960BD242 95586B08 4FABE9D5
  9D8C7908 F056B8F3 94B42407 55A8A66D 31313F45 C56C72BF 8FCE46F6 7146D208
  FC88A75D 0B1D86AA F98312F2 E5DE2821 71EF4274 84A6F891 4B97D6F3 22870629
  5E5C74D4 3D077BE1 BFF6D049 44E4F58D B836C063 678F6751 26E07174 96E0AED6
  0F1CD138 254B0203 010001A3 53305130 0F060355 1D130101 FF040530 030101FF
  301F0603 551D2304 18301680 14F26C20 F6D0F79B 1F6B3B70 D5DCE73D 23DD1DFF
  A9301D06 03551D0E 04160414 F26C20F6 D0F79B1F 6B3B70D5 DCE73D23 DD1DFFA9
  300D0609 2A864886 F70D0101 05050003 82010100 D8FDDC72 7DB07D84 E7505193
  5B9CF003 D33A4DD5 92EA0B77 D14764D4 6966B91F 47D7351A 68798AE5 084A68D5
  FC48DAAC 6C0ADC82 F3985C75 FC8AA04F 01D88CBE 49E26FFC 38BB1428 3B471463
  2654C75C 2B3B586B C7F81D3E 34CD5430 9C676983 C5E235BB 9236A941 EE1D5659
  47439D57 383F8DF1 31302609 414CD288 63A055A3 9256628C 94C24724 E288191B
  BE0C8BC1 4ADA224E A556879F 81A501AB E4D6546F A80B1CF4 F8C1F230 36A623BB
  201D7EAA 21C08B7D C9C01B90 9D9C5388 109D006C B35E0773 EB15D914 681132FA
  698DFDC3 2298B806 F93BFFA9 AB48A1AB 83449739 32ED2A19 30787169 AE0BB353
  37A38DC2 FCF1CD16 D7CA4ADF 950C9E43 0CD00A7C
        quit
!
!
license boot level network-advantage addon dna-advantage
memory free low-watermark processor 131040
!
diagnostic bootup level minimal
!
spanning-tree mode rapid-pvst
spanning-tree portfast bpduguard default
spanning-tree extend system-id
spanning-tree vlan 1-4094 priority 4096
!
!
!
!
username msadmin password 7 14241E021C497972766501302652
!
redundancy
 mode sso
crypto engine compliance shield disable
!
!
!
!
!
transceiver type all
 monitoring
!
vlan 4
 name users
!
vlan 6
 name Server-Mgmt
!
vlan 8
 name voice
!
vlan 20
 name NW-mgmt
!
vlan 30
 name transit
!
vlan 220
 name Cameras
!
lldp run
!
class-map match-any system-cpp-police-ewlc-control
  description EWLC Control
class-map match-any system-cpp-police-topology-control
  description Topology control
class-map match-any system-cpp-police-sw-forward
  description Sw forwarding, L2 LVX data packets, LOGGING, Transit Traffic
class-map match-any system-cpp-default
  description EWLC Data, Inter FED Traffic
class-map match-any system-cpp-police-sys-data
  description Openflow, Exception, EGR Exception, NFL Sampled Data, RPF Failed
class-map match-any system-cpp-police-punt-webauth
  description Punt Webauth
class-map match-any system-cpp-police-l2lvx-control
  description L2 LVX control packets
class-map match-any system-cpp-police-forus
  description Forus Address resolution and Forus traffic
class-map match-any system-cpp-police-multicast-end-station
  description MCAST END STATION
class-map match-any system-cpp-police-high-rate-app
  description High Rate Applications
class-map match-any system-cpp-police-multicast
  description MCAST Data
class-map match-any system-cpp-police-l2-control
  description L2 control
class-map match-any system-cpp-police-dot1x-auth
  description DOT1X Auth
class-map match-any system-cpp-police-data
  description ICMP redirect, ICMP_GEN and BROADCAST
class-map match-any system-cpp-police-stackwise-virt-control
  description Stackwise Virtual OOB
class-map match-any non-client-nrt-class
class-map match-any system-cpp-police-routing-control
  description Routing control and Low Latency
class-map match-any system-cpp-police-protocol-snooping
  description Protocol snooping
class-map match-any system-cpp-police-dhcp-snooping
  description DHCP snooping
class-map match-any system-cpp-police-ios-routing
  description L2 control, Topology control, Routing control, Low Latency
class-map match-any system-cpp-police-system-critical
  description System Critical and Gold Pkt
class-map match-any system-cpp-police-ios-feature
  description ICMPGEN,BROADCAST,ICMP,L2LVXCntrl,ProtoSnoop,PuntWebauth,MCASTData,Transit,DOT1XAuth,Swfwd,LOGGING,L2LVXData,ForusTraffic,ForusARP,McastEndStn,Openflow,Exception,EGRExcption,NflSampled,RpfFailed
!
policy-map system-cpp-policy
!
!
!
!
!
!
!
!
!
!
!
!
interface GigabitEthernet0/0
 vrf forwarding Mgmt-vrf
 no ip address
 shutdown
 negotiation auto
!
interface GigabitEthernet1/0/1
 switchport access vlan 4
 switchport mode access
!
interface GigabitEthernet1/0/2
 switchport access vlan 4
 switchport mode access
!
interface GigabitEthernet1/0/3
!
interface GigabitEthernet1/0/4
!
interface GigabitEthernet1/0/5
!
interface GigabitEthernet1/0/6
!
interface GigabitEthernet1/0/7
!
interface GigabitEthernet1/0/8
!
interface GigabitEthernet1/0/9
!
interface GigabitEthernet1/0/10
!
interface GigabitEthernet1/0/11
!
interface GigabitEthernet1/0/12
!
interface GigabitEthernet1/0/13
!
interface GigabitEthernet1/0/14
!
interface GigabitEthernet1/0/15
!
interface GigabitEthernet1/0/16
!
interface GigabitEthernet1/0/17
!
interface GigabitEthernet1/0/18
!
interface GigabitEthernet1/0/19
!
interface GigabitEthernet1/0/20
!
interface GigabitEthernet1/0/21
!
interface GigabitEthernet1/0/22
!
interface GigabitEthernet1/0/23
!
interface GigabitEthernet1/0/24
!
interface GigabitEthernet1/0/25
!
interface GigabitEthernet1/0/26
!
interface GigabitEthernet1/0/27
!
interface GigabitEthernet1/0/28
!
interface GigabitEthernet1/0/29
!
interface GigabitEthernet1/0/30
!
interface GigabitEthernet1/0/31
!
interface GigabitEthernet1/0/32
!
interface GigabitEthernet1/0/33
!
interface GigabitEthernet1/0/34
!
interface GigabitEthernet1/0/35
!
interface GigabitEthernet1/0/36
!
interface GigabitEthernet1/0/37
 description Primary-InsideFirewall-port2
 switchport access vlan 20
 switchport mode access
!
interface GigabitEthernet1/0/38
 description linktofirewall_port3
 switchport access vlan 20
 switchport mode access
!
interface GigabitEthernet1/0/39
!
interface GigabitEthernet1/0/40
!
interface GigabitEthernet1/0/41
!
interface GigabitEthernet1/0/42
!
interface GigabitEthernet1/0/43
 description link-to-LBJ-F1IDF-SW1
 switchport mode trunk
 spanning-tree bpduguard disable
!
interface GigabitEthernet1/0/44
 description link-to-LBJ-F2IDF-SW1
 switchport mode trunk
 duplex full
 spanning-tree bpduguard disable
!
interface GigabitEthernet1/0/45
 description link-to-LBJ-F6IDF-SW1
 switchport mode trunk
 spanning-tree bpduguard disable
!
interface GigabitEthernet1/0/46
 description link-to-LBJ-F6IDF-SW2
 switchport mode trunk
 spanning-tree bpduguard disable
!
interface GigabitEthernet1/0/47
 description link-to-LBJ-F6IDF-SW3
 switchport mode trunk
 spanning-tree bpduguard disable
!
interface GigabitEthernet1/0/48
 description link-to-LBJ-F6IDF-SW4
 switchport mode trunk
 spanning-tree bpduguard disable
!
interface GigabitEthernet1/1/1
!
interface GigabitEthernet1/1/2
!
interface GigabitEthernet1/1/3
!
interface GigabitEthernet1/1/4
!
interface TenGigabitEthernet1/1/1
 description link-to-LBJ-F1IDF-SW1
 switchport mode trunk
 spanning-tree bpduguard disable
!
interface TenGigabitEthernet1/1/2
 description link-to-LBJ-F2IDF-SW1
 switchport mode trunk
 spanning-tree bpduguard disable
!
interface TenGigabitEthernet1/1/3
 description link-to-LBJ-F6IDF-SW1
 switchport mode trunk
 spanning-tree bpduguard disable
!
interface TenGigabitEthernet1/1/4
 description link-to-LBJ-F6IDF-SW2
 switchport mode trunk
 spanning-tree bpduguard disable
!
interface TenGigabitEthernet1/1/5
 description link-to-LBJ-F6IDF-SW3
 switchport mode trunk
 spanning-tree bpduguard disable
!
interface TenGigabitEthernet1/1/6
 description link-to-LBJ-F6IDF-SW4
 switchport mode trunk
 spanning-tree bpduguard disable
!
interface TenGigabitEthernet1/1/7
!
interface TenGigabitEthernet1/1/8
!
interface FortyGigabitEthernet1/1/1
!
interface FortyGigabitEthernet1/1/2
!
interface TwentyFiveGigE1/1/1
!
interface TwentyFiveGigE1/1/2
!
interface AppGigabitEthernet1/0/1
!
interface Vlan1
 no ip address
!
interface Vlan4
 ip address 10.202.4.1 255.255.255.0
 ip helper-address 10.202.6.10
!
interface Vlan6
 ip address 10.202.6.1 255.255.255.0
 ip helper-address 10.202.6.10
!
interface Vlan8
 ip address 10.202.8.1 255.255.255.0
 ip helper-address 10.202.6.10
!
interface Vlan20
 ip address 10.202.20.1 255.255.255.0
 ip helper-address 10.202.6.10
!
interface Vlan30
 ip address 10.202.30.1 255.255.255.0
!
interface Vlan220
 ip address 10.202.220.1 255.255.255.0
!
ip forward-protocol nd
no ip http server
no ip http secure-server
ip route 0.0.0.0 0.0.0.0 10.202.50.2
ip ssh version 2
!
!
!
!
!
!
!
!
control-plane
 service-policy input system-cpp-policy
!
banner motd ^C
***********************************************************
* ACCESS IS RESTRICTED TO AUTHORIZED PERSONNEL ONLY       *
*                                                         *
* Unauthorized access to this system is prohibited and    *
* subject to criminal and civil penalties. Any access or  *
* other connection to this network without the expressed  *
* permission of management is strictly prohibited. All    *
* unauthorized users will be deemed to be trespassing and *
* will be prosecuted to the fullest extent of the law.    *
***********************************************************
^C
!
line con 0
 privilege level 15
 logging synchronous
 stopbits 1
line vty 0 4
 privilege level 15
 logging synchronous
 transport input ssh
line vty 5 15
 privilege level 15
 logging synchronous
 transport input ssh
line vty 16 31
 transport input ssh
!
call-home
 ! If contact email address in call-home is configured as sch-smart-licensing@cisco.com
 ! the email address configured in Cisco Smart License Portal will be used as contact email address to send SCH notifications.
 contact-email-addr sch-smart-licensing@cisco.com
 profile "CiscoTAC-1"
  active
  destination transport-method http
!
!
!
!
!
!
end

LBJ-COR-SW1#
LBJ-COR-SW1#
LBJ-COR-SW1#sh vl
LBJ-COR-SW1#sh vlan

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Gi1/0/3, Gi1/0/4, Gi1/0/5
                                                Gi1/0/6, Gi1/0/7, Gi1/0/8
                                                Gi1/0/9, Gi1/0/10, Gi1/0/11
                                                Gi1/0/12, Gi1/0/13, Gi1/0/14
                                                Gi1/0/15, Gi1/0/16, Gi1/0/17
                                                Gi1/0/18, Gi1/0/19, Gi1/0/20
                                                Gi1/0/21, Gi1/0/22, Gi1/0/23
                                                Gi1/0/24, Gi1/0/25, Gi1/0/26
                                                Gi1/0/27, Gi1/0/28, Gi1/0/29
                                                Gi1/0/30, Gi1/0/31, Gi1/0/32
                                                Gi1/0/33, Gi1/0/34, Gi1/0/35
                                                Gi1/0/36, Gi1/0/39, Gi1/0/40
                                                Gi1/0/41, Gi1/0/42, Gi1/0/43
                                                Gi1/0/44, Te1/1/1, Te1/1/2
                                                Te1/1/5, Te1/1/6, Te1/1/7
                                                Te1/1/8, Ap1/0/1
4    users                            active    Gi1/0/1, Gi1/0/2
6    Server-Mgmt                      active
8    voice                            active
20   NW-mgmt                          active    Gi1/0/37, Gi1/0/38

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
30   transit                          active
220  Cameras                          active
1002 fddi-default                     act/unsup
1003 token-ring-default               act/unsup
1004 fddinet-default                  act/unsup
1005 trnet-default                    act/unsup

VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
1    enet  100001     1500  -      -      -        -    -        0      0
4    enet  100004     1500  -      -      -        -    -        0      0
6    enet  100006     1500  -      -      -        -    -        0      0
8    enet  100008     1500  -      -      -        -    -        0      0
20   enet  100020     1500  -      -      -        -    -        0      0
30   enet  100030     1500  -      -      -        -    -        0      0
220  enet  100220     1500  -      -      -        -    -        0      0
1002 fddi  101002     1500  -      -      -        -    -        0      0
1003 tr    101003     1500  -      -      -        -    -        0      0
1004 fdnet 101004     1500  -      -      -        ieee -        0      0
1005 trnet 101005     1500  -      -      -        ibm  -        0      0

Remote SPAN VLANs
------------------------------------------------------------------------------


LBJ-COR-SW1#sh lldp nei
LBJ-COR-SW1#sh lldp neighbors
Capability codes:
    (R) Router, (B) Bridge, (T) Telephone, (C) DOCSIS Cable Device
    (W) WLAN Access Point, (P) Repeater, (S) Station, (O) Other

Device ID           Local Intf     Hold-time  Capability      Port ID
cida341-lbj-fw1     Gi1/0/38       120        R               port5

Total entries displayed: 1

LBJ-COR-SW1#sh int st
LBJ-COR-SW1#sh int statu
LBJ-COR-SW1#sh int status

Port         Name               Status       Vlan       Duplex  Speed Type
Gi1/0/1                         notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/2                         notconnect   4            auto   auto 10/100/1000BaseTX
Gi1/0/3                         notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/4                         notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/5                         notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/6                         notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/7                         notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/8                         notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/9                         notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/10                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/11                        notconnect   1            auto   auto 10/100/1000BaseTX

Port         Name               Status       Vlan       Duplex  Speed Type
Gi1/0/12                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/13                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/14                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/15                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/16                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/17                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/18                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/19                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/20                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/21                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/22                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/23                        notconnect   1            auto   auto 10/100/1000BaseTX

Port         Name               Status       Vlan       Duplex  Speed Type
Gi1/0/24                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/25                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/26                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/27                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/28                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/29                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/30                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/31                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/32                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/33                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/34                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/35                        notconnect   1            auto   auto 10/100/1000BaseTX

Port         Name               Status       Vlan       Duplex  Speed Type
Gi1/0/36                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/37     Primary-InsideFire connected    20         a-full a-1000 10/100/1000BaseTX
Gi1/0/38     linktofirewall_por connected    20         a-full a-1000 10/100/1000BaseTX
Gi1/0/39                        connected    1          a-full a-1000 10/100/1000BaseTX
Gi1/0/40                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/41                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/42                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/43     link-to-LBJ-F1IDF- notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/44     link-to-LBJ-F2IDF- notconnect   1            full   auto 10/100/1000BaseTX
Gi1/0/45     link-to-LBJ-F6IDF- connected    trunk      a-full a-1000 10/100/1000BaseTX
Gi1/0/46     link-to-LBJ-F6IDF- connected    trunk      a-full a-1000 10/100/1000BaseTX
Gi1/0/47     link-to-LBJ-F6IDF- connected    trunk      a-full a-1000 10/100/1000BaseTX
 --More--
[Connection to 10.202.20.1 closed by foreign host]
LBJ-F6IDF-SW3#
