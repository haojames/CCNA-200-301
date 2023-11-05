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

Ethernet trunk interface (Switchport mode { mode})hỗ trợ nhiều loại Trunking khác nhau
- Access : đặt interface tương ứng luôn ở chế độ nontrunking (access port)
- Dynamic desirable (default mode on Catalyst 2950 and 3550): đặt interface tương ứng ở trạng thái "thử" chuyển the link sang trunk link. Interface khi đuợc cấu hình thế này sẽ chuyển sang mode trunk nếu interface láng giềng được set thành trunk, desirable, hay auto mode. Nếu interface láng giềng được set thành access hay non-negotiate thì "the link" sẽ trở thành non-trunking link, of course ! :lol:
- Dynamic auto: đặt interface sẵn sàng trở thành để chuyển từ 'the link' sang trunk link nếu interface láng giềng được set là trunk, hay desirable mode. Trường hợp không phải là các mode này, tất nhiên interface này sẽ ở mode non-trunking link
- Trunk : đặt interface luôn ở mode trunk và thương lượng để chuyển the link sang trunk link, interface luôn ở mode trunk cho dù interface láng giềng không đồng ý thay đổi trạng thái
- Non-negotiate: ngăn interface tạo ra DTP frame. Chỉ sử dụng lệnh này nếu interface switchport mode là access hay trunk.
- dotq-tunnel (Not an option on the Catalyst 2950.)

###
    Mỗi port trên switch có thể được cấu hình ở 1 trong 3 mode: Access, Trunk và Tunnel.
    Với "switchport mode access", port sẽ ở mode access vô điều kiện.
    Với "switchport mode trunk", port sẽ ở mode trunk vô điều kiện.
    Với "switchport mode dot1q-tunnel", port sẽ ở mode tunnel vô điều kiện.
    Với "switchport mode dynamic auto|desirable", port sẽ ở mode access hay trunk còn tùy thuộc vào mode của remote port, cụ thể như sau:

- auto | access ----> mode access
- auto | auto ----> mode access
- auto | desirable ----> mode trunk
- auto | trunk ----> mode trunk

- desirable | access ----> mode access
- desirable | auto ----> mode trunk
- desirable | desirable ----> mode trunk
- desirable | trunk ----> mode trunk


- NOTE: When configuring port security, by default the learned MAC addresses are flushed when the switch is reloaded. To prevent this and ensure that the switch preserves MAC addresses that are dynamically learned via port security, you need to configure sticky learning. This configuration, in conjunction with the copy run start command, saves the learned MAC addresses to NVRAM. This means that when the
switch is rebooted, the MAC addresses learned are not lost. The switch adds the switchport port-security mac-address sticky <mac-address> command dynamically under the interface for every sticky dynamically learned MAC address. So if 100 MAC addresses are learned this way, the switch would add 100 of these statements after the switchport port-security mac-address sticky command that you issued under the
interface. Be very careful because this can create a very large configuration file in the real world