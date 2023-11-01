# Detail
    SW1(F0/1) -> <- SW2(F0/1)
# Script

## Task 1
    In preparation for VLAN configuration, configure a hostname on Sw1 as well as the VLANs depicted in the topology.
    ```C++
    Switch#config t
    Enter configuration commands, one per line. End with CTRL/Z.
    Switch(config)#hostname Sw1
    Sw1(config)#vlan10
    Sw1(config-vlan)#name SALES
    Sw1(config-vlan)#exit
    Sw1(config)#vlan20
    Sw1(config-vlan)#name MANAGERS
    Sw1(config-vlan)#exit
    Sw1(config)#vlan30
    Sw1(config-vlan)#name ENGINEERS
    Sw1(config-vlan)#exit
    Sw1(config)#vlan40
    Sw1(config-vlan)#name SUPPORT
    ```
## Task 2
    Configure ports FastEthernet0/5 to FastEthernet0/8 as access ports and assign them to the VLANs specified.
    ```C++
    Sw1(config)#interface fastethernet0/5
    Sw1(config-if)#switchport mode access
    Sw1(config-if)#switchport access vlan10
    Sw1(config-if)#exit
    Sw1(config)#interface fastethernet0/6
    Sw1(config-if)#switchport mode access
    Sw1(config-if)#switchport access vlan20
    Sw1(config-if)#exit
    Sw1(config)#interface fastethernet0/7
    Sw1(config-if)#switchport mode access
    Sw1(config-if)#switchport access vlan30
    Sw1(config-if)#exit
    Sw1(config)#interface fastethernet0/8
    Sw1(config-if)#switchport mode access
    Sw1(config-if)#switchport access vlan40
    ```
## Task 3
    Verify your VLAN configuration using relevant show commands in Cisco IOS
    -> show vlan brief

## Report
```c++
Top Assembly Revision Number    : B0
Version ID                      : V02
CLEI Code Number                : COM3K00BRA
Hardware Board Revision Number  : 0x01


Switch   Ports  Model              SW Version              SW Image
------   -----  -----              ----------              ----------
*    1   26     WS-C2960-24TT      12.2                    C2960-LANBASE-M

Cisco IOS Software, C2960 Software (C2960-LANBASE-M), Version 12.2(25)FX, RELEASE SOFTWARE (fc1)
Copyright (c) 1986-2005 by Cisco Systems, Inc.
Compiled Wed 12-Oct-05 22:05 by pt_team

Press RETURN to get started!


%LINK-5-CHANGED: Interface FastEthernet0/1, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet0/1, changed state to up


Switch>conf
Switch>conf t
Switch>conf t
            ^
% Invalid input detected at '^' marker.
	
Switch>enable
Switch#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Switch(config)#hostname SW1
SW1(config)#vlan 10
SW1(config-vlan)#name
SW1(config-vlan)#name SALES
SW1(config-vlan)#exit
SW1(config)#vlan 20
SW1(config-vlan)#name MANAGERS
SW1(config-vlan)#exit
SW1(config)#vlan 30
SW1(config-vlan)#name ENGINEERS
SW1(config-vlan)#exit
SW1(config)#vlan 40
SW1(config-vlan)#name SUPPORT
SW1(config-vlan)#exit
SW1(config)#show vla
SW1(config)#show vla
SW1(config)#exit
SW1#
%SYS-5-CONFIG_I: Configured from console by console

SW1#show vl
SW1#show vlan 
SW1#show vlan br
SW1#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Fa0/1, Fa0/2, Fa0/3, Fa0/4
                                                Fa0/5, Fa0/6, Fa0/7, Fa0/8
                                                Fa0/9, Fa0/10, Fa0/11, Fa0/12
                                                Fa0/13, Fa0/14, Fa0/15, Fa0/16
                                                Fa0/17, Fa0/18, Fa0/19, Fa0/20
                                                Fa0/21, Fa0/22, Fa0/23, Fa0/24
                                                Gig0/1, Gig0/2
10   SALES                            active    
20   MANAGERS                         active    
30   ENGINEERS                        active    
40   SUPPORT                          active    
1002 fddi-default                     active    
1003 token-ring-default               active    
1004 fddinet-default                  active    
1005 trnet-default                    active    
SW1#
%LINK-3-UPDOWN: Interface FastEthernet0/1, changed state to down

%LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet0/1, changed state to down

%LINK-5-CHANGED: Interface FastEthernet0/1, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet0/1, changed state to up

SW1#conf
SW1#configure t
SW1#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
SW1(config)#inter
SW1(config)#interface fast
SW1(config)#interface fastEthernet 0/5
SW1(config-if)#sw
SW1(config-if)#switchport acc
SW1(config-if)#switchport access mode
                                 ^
% Invalid input detected at '^' marker.
	
SW1(config-if)#switchport mode acce
SW1(config-if)#switchport mode access
SW1(config-if)#sw
SW1(config-if)#switchport acc
SW1(config-if)#switchport access vlan 10
SW1(config-if)#exit
SW1(config)#inter
SW1(config)#interface fas
SW1(config)#interface fastEthernet 0/6
SW1(config-if)#sw
SW1(config-if)#switchport acce
SW1(config-if)#switchport access vl
SW1(config-if)#switchport mode acc
SW1(config-if)#switchport mode access
SW1(config-if)#sww
SW1(config-if)#sww
SW1(config-if)#swu
SW1(config-if)#swi
SW1(config-if)#switchport acc
SW1(config-if)#switchport access vlan20
                                     ^
% Invalid input detected at '^' marker.
	
SW1(config-if)#switchport access vlan 20
SW1(config-if)#exit
SW1(config)#inter
SW1(config)#interface fas
SW1(config)#interface fastEthernet 0/7
SW1(config-if)#sw
SW1(config-if)#switchport ac
SW1(config-if)#switchport access mode
                                 ^
% Invalid input detected at '^' marker.
	
SW1(config-if)#switchport mode acc
SW1(config-if)#switchport mode access
SW1(config-if)#sw
SW1(config-if)#switchport acce
SW1(config-if)#switchport access vlan 30
SW1(config-if)#exit
SW1(config)#inter
SW1(config)#interface fa
SW1(config)#interface fastEthernet 0/8
SW1(config-if)#sw
SW1(config-if)#switchport mode acces
SW1(config-if)#switchport mode access
SW1(config-if)#sw
SW1(config-if)#switchport acc
SW1(config-if)#switchport access vlan 40
SW1(config-if)#exit
SW1(config)#exit
SW1#
%SYS-5-CONFIG_I: Configured from console by console

SW1#show vla
SW1#show vlan br
SW1#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Fa0/1, Fa0/2, Fa0/3, Fa0/4
                                                Fa0/9, Fa0/10, Fa0/11, Fa0/12
                                                Fa0/13, Fa0/14, Fa0/15, Fa0/16
                                                Fa0/17, Fa0/18, Fa0/19, Fa0/20
                                                Fa0/21, Fa0/22, Fa0/23, Fa0/24
                                                Gig0/1, Gig0/2
10   SALES                            active    Fa0/5
20   MANAGERS                         active    Fa0/6
30   ENGINEERS                        active    Fa0/7
40   SUPPORT                          active    Fa0/8
1002 fddi-default                     active    
1003 token-ring-default               active    
1004 fddinet-default                  active    
1005 trnet-default                    active    
SW1#
```
