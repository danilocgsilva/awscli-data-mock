import sys
import math
from random import random
# from awsclimock.AWS_General_Entities_Mocker import AWS_General_Entities_Mocker


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

