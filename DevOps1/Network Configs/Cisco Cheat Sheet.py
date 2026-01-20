##############################################
# Project:        Network Configurations/Cheat Sheets
# File:           Cisco_Cheat_Sheet.py
# Author:         Jonathan Hernandez
# Created:        2025-08-18
# Last Modified:  2025-09-05
# Version:        1.4
# Description:    Cisco Cheat Sheet - Common commands for Cisco network devices
#
# Notes:
# - Quick reference for Cisco switch/router CLI commands
# - Grouped by category for readability
##############################################

# ===============================
# DAY-0: BRAND NEW CATALYST 9300X
# ===============================

# Out-of-Band Mgmt (Mgmt-vrf on Gi0/0)
enable
configure terminal
 hostname SW-9300X-01
 ip domain-name randa.local
 crypto key generate rsa modulus 2048
 ip ssh version 2
 username netadmin privilege 15 secret <STRONG_SECRET>
 enable secret <ENABLE_SECRET>
 aaa new-model
 aaa authentication login default local
 aaa authorization exec default local

 line console 0
  login local
  exec-timeout 10 0

 line vty 0 4
  transport input ssh
  login local
  exec-timeout 10 0

 interface GigabitEthernet0/0
  vrf forwarding Mgmt-vrf
  ip address <MGMT_IP> <MASK>
  no shutdown

 ip route vrf Mgmt-vrf 0.0.0.0 0.0.0.0 <GATEWAY>

 clock timezone CST -6
 clock summer-time CDT recurring
 ntp server vrf Mgmt-vrf <NTP_SERVER> prefer
 logging host vrf Mgmt-vrf <SYSLOG_SERVER>
 logging trap informational

# Enable STP protections
spanning-tree mode rapid-pvst
spanning-tree portfast default
spanning-tree bpduguard default
errdisable recovery cause bpduguard
errdisable recovery interval 60

# Save configuration
end
write memory


# ===============================
# VLAN CONFIGURATION (L2)
# ===============================

# Assign VLAN to port
Switch(config)# interface fa0/1
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 2

# Remove VLANs
device(config)# interface ethernet 1/1/1
device(config-if)# vlan-config remove all
device(config-if)# vlan-config remove all 2000 to 2005

# Create/Configure VLAN
Switch(config)# vlan 5
Switch(config-vlan)# name accounting
Switch(config-vlan)# state active
Switch(config-vlan)# no shutdown

# Delete VLAN
Switch(config)# no vlan <vlan-id>

# Show VLANs
show vlan
show vlan id 10
show interfaces switchport


# ===============================
# INTERFACE VLAN (SVI) CONFIG (L3)
# ===============================

Switch(config)# ip routing
Switch(config)# interface vlan 10
Switch(config-if)# description User VLAN 10 SVI
Switch(config-if)# ip address 10.10.10.1 255.255.255.0
Switch(config-if)# no shutdown

# DHCP relay
Switch(config-if)# ip helper-address 10.10.0.10

# HSRP redundancy
Switch(config)# interface vlan 10
Switch(config-if)# standby 10 ip 10.10.10.1
Switch(config-if)# standby 10 priority 110
Switch(config-if)# standby 10 preempt

# VRRP redundancy
Switch(config)# interface vlan 10
Switch(config-if)# vrrp 10 ip 10.10.10.1
Switch(config-if)# vrrp 10 priority 110
Switch(config-if)# vrrp 10 preempt

# Verify
show ip interface brief | include Vlan
show standby brief
show vrrp brief


# ===============================
# INTERFACE COMMANDS
# ===============================

show interface status
show run int gi1/0/44
no switchport access vlan <vlan_id>
show interface gi1/0/1 switchport
show interfaces trunk
show interface gi1/0/1 counters errors
show interface gi1/0/1 | include rate


# ===============================
# MAC ADDRESS TABLE
# ===============================

show mac address-table
show mac address-table interface gi1/0/1
show mac address-table | include <mac>


# ===============================
# DEVICE INFORMATION
# ===============================

show version
show lldp neighbors
show cdp neighbor
show power inline
show environmental all
show interface link

# ===============================
# BASIC CONFIGURATION
# ===============================

Switch(config)# hostname <HOSTNAME>
Switch(config)# interface fa0/1
Switch(config-if)# speed 100
Switch(config-if)# duplex full
Switch(config)# copy running-config startup-config

# Ping from VLAN interface
ping -i vlan-interface 5 <ip>


# ===============================
# MONITORING & LOGGING
# ===============================

show users
show users all
disconnect { console | ip_address }
*terminal monitor*
show logging
show logging buffer
show logging | inc LINK-3-UPDOWN


# ===============================
# NETWORK SNIFFING / PACKET CAPTURE
# ===============================

# SPAN
monitor session 1 source interface gi1/0/1
monitor session 1 destination interface gi1/0/48
no monitor session 1

# Embedded Packet Capture
monitor capture CAP1 interface gi1/0/1 both
monitor capture CAP1 start
monitor capture CAP1 stop
monitor capture CAP1 export flash:capture.pcap
show monitor capture CAP1 buffer brief


# ===============================
# ROUTING & IP TROUBLESHOOTING
# ===============================

show ip route
show arp
ping <ip>
traceroute <ip>y
show ip interface brief
show running-config | include interface Vlan|ip address


# ===============================
# ACLs & OPEN PORTS
# ===============================

show access-lists
ip access-group <ACL_NAME> in
ip access-group <ACL_NAME> out
show access-lists | include matches
show control-plane host open-ports


# ===============================
# DEBUGGING TOOLS (USE WITH CARE)
# ===============================

debug ip packet
debug spanning-tree events
debug cdp packets
undebug all


# ===============================
# QOS & TRAFFIC ANALYSIS
# ===============================

show policy-map interface
show queueing interface gi1/0/1
show ip cache flow
show ip flow top-talkers


# ===============================
# SYSTEM HEALTH / UTILIZATION
# ===============================

show running-config
show startup-config
show clock
show processes cpu sorted
show processes memory


# ===============================
# TROUBLESHOOTING PLAYBOOKS
# ===============================

# Interface down/flapping
show interface status | include Gi1/0/1
show interface gi1/0/1
show logging | inc Gi1/0/1
# Fix: check cable, VLAN, STP, errors

# Inter-VLAN routing fails
show ip interface brief | include Vlan
show ip route | include subnet
ping gateway
# Fix: ensure ip routing, SVI up, redundancy OK

# Trunk mismatch
show interfaces trunk
show cdp neighbor detail | include VLAN
# Fix: match allowed/native VLANs

# High errors/drops
show interface gi1/0/1 counters errors
# Fix: check duplex, bad cable, QoS drops


interface GigabitEthernet1/0/33
 description user-phone
 switchport access vlan 4
 switchport mode access
 switchport voice vlan 55
 shutdown
 spanning-tree portfast
 spanning-tree link-type point-to-point

router bgp 64513
  address-family ipv4
   neighbor 169.254.96.49 remote-as 64521
   neighbor 169.254.96.49 password 0xliPBrp11cTsZWQdv2TUnUq
   network " " ! --> Prefixes you want to advertise over this Virtual Interface
exit