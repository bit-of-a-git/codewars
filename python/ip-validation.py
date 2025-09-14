import ipaddress


def is_valid_IP(strng):
    try:
        ipaddress.ip_address(strng)
        return True
    except:
        return False
