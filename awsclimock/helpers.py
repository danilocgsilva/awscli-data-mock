import sys
import math
from random import random


def get_command_to_mock() -> str:

    try:
        command = sys.argv[1]
    except IndexError:
        command = ask_command()

    return command


def ask_command():
    return input("Which AWS command do you wish to mock? Please, type the command name: ")


def get_exadecimal_sample(num) -> str:
    possibilities = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    hexadecimalcode = ""

    for x in range(num):
        hexadecimalcode += possibilities[math.floor(random() * len(possibilities))]

    return hexadecimalcode


def random_until_255() -> str:
    result_random = math.ceil(random() * 255)
    return str(result_random)


def get_mac_address() -> str:
    mac_address_parts = []
    for x in range(6):
        mac_address_parts.append(get_exadecimal_sample(2))
    return ":".join(mac_address_parts)


def get_mocked_network_interface_data(
    security_group_id: str, 
    owner_id: str, 
    private_ip: str,
    subnet_id: str,
    vpc_id: str
) -> dict:
    return {
        "Attachment": {
            "AttachTime": "2018-10-18T00:44:48.000Z",
            "AttachmentId": "eni-attach-" + get_exadecimal_sample(17),
            "DeleteOnTermination": True,
            "DeviceIndex": 0,
            "Status": "attached"
        },
        "Description": "",
        "Groups": [
            {
                "GroupName": "default",
                "GroupId": security_group_id
            }
        ],
        "Ipv6Addresses": [],
        "MacAddress": get_mac_address(),
        "NetworkInterfaceId": "eni-" + get_exadecimal_sample(17),
        "OwnerId": owner_id,
        "PrivateDnsName": "ip-" + private_ip.replace(".", "-") + ".ec2.internal",
        "PrivateIpAddress": private_ip,
        "PrivateIpAddresses": [
            {
                "Primary": True,
                "PrivateDnsName": "ip-" + private_ip.replace(".", "-") + ".ec2.internal",
                "PrivateIpAddress": private_ip
            }
        ],
        "SourceDestCheck": True,
        "Status": "in-use",
        "SubnetId": subnet_id,
        "VpcId": vpc_id,
        "InterfaceType": "interface"
    }

