import ipaddress
# Nhập địa chỉ IP và Subnet dưới dạng chuỗi
ip_address = "172.16.0.1"
subnet = "172.16.0.1/27"  # Địa chỉ IP và Subnet
# Chuyển đổi địa chỉ IP và Subnet thành các đối tượng IP và Network
ip = ipaddress.IPv4Address(ip_address)
network = ipaddress.IPv4Network(subnet, strict=False)
# Lấy Subnet Mask từ đối tượng Network
subnet_mask = network.netmask
# In Subnet Mask
print(f"Subnet Mask: {subnet_mask}")
    