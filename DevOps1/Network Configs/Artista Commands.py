
enable
show interfaces


show interfaces ethernet19

# show vlan 10

switch(config)# interface Ethernet 1-3
switch(config-if-Et1-3)# switchport mode access
switch(config-if-Et1-3)# switchport access vlan 23
switch(config-if-Et1-3)# show interfaces ethernet 1-3 vlans
Port       Untagged Tagged
Et1        None     23,25
Et2        18       -
Et3        None     14
switch(config-if-Et1-3)#
