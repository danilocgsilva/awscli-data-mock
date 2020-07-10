import math
from random import random
from awsclimock.IpPermissionGenerator import IpPermissionGenerator
from awsclimock.TagGenerator import TagGenerator

class SecurityGroupDataGenerator:

    def get_ip_permissions(num: int):
        
        ip_permissions = []

        for x in range(num):
            ip_permissions.append(IpPermissionGenerator.get_ip_permission())

        return ip_permissions


    def get_owner_id():

        owner_id = ""
        for x in range(12):
            owner_id += str(math.ceil(random() * 10))

        return owner_id


    def get_group_id():
        return "sg-" + SecurityGroupDataGenerator.get_exadecimal_sample(17)


    def get_tags(num: int):

        tags = []

        for x in range(num):
            tags.append(TagGenerator.get_tag())

        return tags


    def get_vpc_id() -> str:
        return "vpc-" + SecurityGroupDataGenerator.get_exadecimal_sample(8)


    def get_exadecimal_sample(num) -> str:

        possibilities = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

        hexadecimalcode = ""

        for x in range(num):
            hexadecimalcode += possibilities[math.floor(random() * len(possibilities))]

        return hexadecimalcode
        

