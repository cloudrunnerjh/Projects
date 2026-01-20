

Building configuration...

Current configuration : 18057 bytes
!
! Last configuration change at 16:56:12 CDT Wed Sep 17 2025 by msadmin
! NVRAM config last updated at 16:56:49 CDT Wed Sep 17 2025 by msadmin
!
version 17.9
service timestamps debug datetime msec localtime show-timezone
service timestamps log datetime msec localtime show-timezone
service password-encryption
service call-home
platform punt-keepalive disable-kernel-core
!
hostname CSC-IDFD-SW1
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
!
!
!
clock timezone CST -6 0
clock summer-time CDT recurring
switch 1 provision c9200l-48p-4x
!
!
!
!
ip routing
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
crypto pki trustpoint SLA-TrustPoint
 enrollment pkcs12
 revocation-check crl
!
crypto pki trustpoint TP-self-signed-2495017187
 enrollment selfsigned
 subject-name cn=IOS-Self-Signed-Certificate-2495017187
 revocation-check none
 rsakeypair TP-self-signed-2495017187
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
crypto pki certificate chain TP-self-signed-2495017187
 certificate self-signed 01
  30820330 30820218 A0030201 02020101 300D0609 2A864886 F70D0101 05050030
  31312F30 2D060355 04031326 494F532D 53656C66 2D536967 6E65642D 43657274
  69666963 6174652D 32343935 30313731 3837301E 170D3234 30383035 32313432
  34395A17 0D333430 38303532 31343234 395A3031 312F302D 06035504 03132649
  4F532D53 656C662D 5369676E 65642D43 65727469 66696361 74652D32 34393530
  31373138 37308201 22300D06 092A8648 86F70D01 01010500 0382010F 00308201
  0A028201 0100B9C5 117A9DEB F001DA95 03A72894 05A0ED47 F757EB2A 91D13C6A
  D81BE23C 1F738972 D85FD71A FC7A253F 06431AB4 9E28607E 18593A15 1E798F40
  F932A3CF EC671733 EA20D259 79A57BDC 01D85F3E BEADEBEC 310A0E77 FC5EB099
  3A6A877C E83AC0FA 6D30C06E 8DC2A3BB B08058E0 8747A36B 2F3C9C92 B98F1BC9
  CB404D9D 341D89AE EFCD5E70 1CA88850 0180F802 B240F9BF 805F2595 82BD3E38
  A9CCA419 5909A1B7 FBBE33C2 0811B701 A88AA3E7 4514BBE9 7D5279BB BEC56404
  75F9FFA7 16F4C5F0 90BF2FD4 1B282E2C 377A27E6 7130B86F ECCB9AAC E2EE3806
  27A33693 85ED9A69 DC0D1495 7F2AD7F1 1058942D 789127A0 ACF5D714 DF09B4EA
  43FCA721 02570203 010001A3 53305130 0F060355 1D130101 FF040530 030101FF
  301F0603 551D2304 18301680 1414334C D82DD3EE AF34673B EAE8B7B7 BC421F79
  26301D06 03551D0E 04160414 14334CD8 2DD3EEAF 34673BEA E8B7B7BC 421F7926
  300D0609 2A864886 F70D0101 05050003 82010100 470938D8 1762A8A3 BAA8EB9C
  E467C4C9 84B85F79 49BC03DA 1E0E03F9 B80CEAB3 8AE607DC B1CA47CD 078E55D5
  350516C0 F355BAF6 0EDFE22E CE1BA497 5AEDBC96 F7B15A3C E0B84C90 2BCA1DEA
  CE96F548 08BAA792 6D8BFF05 A6105AAC E927D004 893B8ECA 26B7980B 18E17FA3
  348C893F 68E9126C CA6B5BAA 780437A1 8030B310 0F46E724 B33062F6 33001A51
  DFC4CBD3 BBAB4E2E 3B8BD696 89011210 0647C29C E0A9402F 4A7237A0 C80A4E36
  5F067252 B56C96E5 B18CC4FC 136CE819 EF203C55 E854E404 9351E47D 1D679ABD
  D805AD3D 10E92559 1526ED64 FA3FF983 D8F1F2AC 2CAAE423 5B59E6FC A6CE2B24
  407807B0 389124C2 74E916E9 5449533B CD716ED2
        quit
!
crypto pki certificate pool
 cabundle nvram:ios_core.p7b
!
license boot level network-essentials addon dna-essentials
memory free low-watermark processor 9899
!
diagnostic bootup level minimal
!
spanning-tree mode rapid-pvst
spanning-tree portfast bpduguard default
spanning-tree extend system-id
!
!
!
enable secret level 2 9 $9$ry8REziayInX1U$jEcZt.sul3SK/rihGODmog5rAIZVope6MgXNZpM8Skw
enable secret 9 $9$9S/XpKg68A3JIE$v2J0MWruTEKAU8gcnx25edxCmBtvz0esxBZQSiENPck
!
username msadmin privilege 15 secret 9 $9$KnNXcBmIeo0UVk$vDwB4WFKQJJEEGxrsfhRw7QFWxl48g3yzn1ZW6.aofQ
username jwilliams privilege 15 secret 9 $9$wodkxOItmS964k$GOlKUhRA.af/hUfqs/j3F8nDg/Zj0SAqHFSl0dbutoo
username tjohnson privilege 15 secret 9 $9$F7cV.qF2wrTaEe$1QG/9JEE9FF99/Sahat9Mx/4PqWRl16pIaVOcw40N6.
username jhernandez privilege 15 secret 9 $9$TAeS99WbRBixPc$7/1tt4asNIjg29Dp.ZidTRSsoAI23QD3vaThhucjGJg
username gvaldez privilege 15 secret 9 $9$SHjyKQmRDSPd8d$bOiADQCnznyj8jWtQuy7KTkf36CMBn2dSdWZmPAMILI
username jaldana privilege 15 secret 9 $9$p1ONO.kAqzmBPz$YZOpFmbUPHLQIi1M45Uz5pZrdkomA02lMAHB31NkgrA
username mmcdonough privilege 15 secret 9 $9$YhdLDgcVPKTrBU$/G38fwRj68.f5VmkUHWzKacPmT3/J0kfXKAkTJEXLPw
username _netbox privilege 2 secret 9 $9$Td722c/ghJHqEE$seshBWwUN1TE2uFDrhkjYoy4JUIIigOgtBDXaFI3ovU
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
vlan 3
 name MDF
!
vlan 4
 name IDF-B
!
vlan 5
 name IDF-A
!
vlan 6
 name Wireless
!
vlan 7
 name Personal_Wireless
!
vlan 8
 name Guest_Wireless
!
vlan 9
 name vlan9-unk
!
vlan 20
 name Management(old)
!
vlan 42
 name Meraki_Mgt
!
vlan 46
 name IDF-C
!
vlan 52
 name WORLD_SOURCE
!
vlan 55
 name RC_VOIP
!
vlan 104
 name Users
!
vlan 106
 name Server-Mgmt
!
vlan 130
 name M-Prod
!
vlan 131
 name M-Mgmt
!
vlan 132
 name M-Endpoints
!
vlan 134
 name M-Test
!
vlan 171
 name Meraki_Prod
!
vlan 172
 name Meraki_Guest
!
vlan 220
 name NW-mgmt
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
  description EWLC data, Inter FED Traffic
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
int range g3/0/1 - 24
switchport access vlan 104
description Users/Phone
switchport mode access
spanning-tree portfast

!
!
!
!
!
!
interface Port-channel1
 description CSC-COR-SW1
 switchport mode trunk
!
interface GigabitEthernet0/0
 vrf forwarding Mgmt-vrf
 no ip address
!
interface GigabitEthernet1/0/1
 description CSC-ST9_SLIP.145
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/2
 description Users-Phone
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/3
 description CSC-ST9-LABEL.150
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/4
 description Users-Phone
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/5
 description CSC-ST6-SLIP.146
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/6
 description Users-Phone
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/7
 description CSC-ST8-LABEL.151
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/8
 description Users-Phone
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/9
 description M715-5SCZK.randa.local
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/10
 description Users-Phone
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/11
 description CSC-ST8-SLIP.149
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/12
 description Users-Phone
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/13
 description M715-J05TN7L.randa.local
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/14
 description Users-Phone
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/15
 description CSC-ST7-LABEL.148
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/16
 description Users-Phone
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/17
 description CSC-ST7-SLIP.147
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/18
 description Users-Phone
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/19
 description CSC-ST6-LABEL.152
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/20
 description Users-Phone
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/21
 description M715-5TN79.randa.local
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/22
 description Users-Phone
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/23
 description Users-Phone
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/24
 description Users-Phone
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/25
 description Users-Phone
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/26
 description Users-Phone
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/27
 description Users-Phone
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/28
 description Users-Phone
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/29
 description FTWWHK028.randa.local
 switchport access vlan 104
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/30
 description Users-Phone
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/31
 description Users-Phone
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/32
 description Users-Phone
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/33
 description Users-Phone
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/34
 description Users-Phone
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/35
 description Users-Phone
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/36
 description Users-Phone
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/37
 description Users-Phone
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/38
 description Users-Phone
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/39
 description Users-Phone
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/40
 description Users-Phone
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/41
 description Users-Phone
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/42
 description Users-Phone
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/43
 description CSC-ST2-LABEL.157
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/44
 description Users-Phone
 switchport access vlan 104
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/45
 description CSC-ST2-Slip.158
 switchport access vlan 106
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/46
 description Users-Phone
 switchport access vlan 104
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/47
 description APC-UPS
 switchport access vlan 104
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/48
 description CSC-REMTECH
 switchport access vlan 104
 switchport mode access
 spanning-tree portfast
!
interface TenGigabitEthernet1/1/1
 description CSC-COR-SW1-1/1/6(Po1)
 switchport mode trunk
 channel-group 1 mode active
!
interface TenGigabitEthernet1/1/2
!
interface TenGigabitEthernet1/1/3
!
interface TenGigabitEthernet1/1/4
!
interface Vlan1
 ip dhcp client client-id ascii cisco-b08d.57eb.afc7-Vl1
 ip address dhcp
!
interface Vlan220
 description NW-mgmt
 ip address 10.206.20.16 255.255.255.0
!
no ip http server
ip http authentication local
no ip http secure-server
ip http client source-interface Vlan1
ip forward-protocol nd
ip route 0.0.0.0 0.0.0.0 10.206.20.1
ip ssh version 2
!
!
!
snmp-server community MS-Randa RO
snmp-server community RAARO RO
!
!
!
control-plane
 service-policy input system-cpp-policy
!
privilege exec level 2 show mac address-table
privilege exec level 2 show mac
privilege exec level 2 show interfaces status
privilege exec level 2 show interfaces
privilege exec level 2 show
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
 logging synchronous
 stopbits 1
line vty 0 4
 logging synchronous
 transport input ssh
line vty 5 15
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
ntp server 10.206.20.1 prefer
!
