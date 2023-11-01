1. By default, Cisco switches are VTP servers so no configuration is necessary for
server mode. Use the show vtp status command to look at the current VTP operating
mode of the switch.
2. "switchport mode access" set interface of switch to "mode" access.
What is mode access ?
    - In access port mode, the port belongs to only one VLAN. All computers plugged into your port belong to that VLAN.
    - Frames sent on the access port will follow the ethernet frame format standard (802.3).
    - Access port is often used when the port is connected to a workstation.
"switchport access vlan10" in interface fastEthernet0/6
access unique vlan 10 can traffic in interface fastEthernet0/6.