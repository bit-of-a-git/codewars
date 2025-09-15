from ipaddress import IPv4Address


def int32_to_ip(int32):
    ipBin = bin(int32)[2:].rjust(32, "0")
    ipStr = []
    for i in range(len(ipBin) // 8):
        octet = ipBin[(i * 8) : ((i + 1) * 8)]
        octet = int(octet, 2)
        ipStr.append(str(octet))
    return ".".join(ipStr)


def int32_to_ip_using_library(int32):
    return str(IPv4Address(int32))
