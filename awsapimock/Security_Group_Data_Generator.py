import math
from random import random
from awsclimock.IpPermissionGenerator import IpPermissionGenerator
from awsclimock.TagGenerator import TagGenerator
from awsclimock.helpers import get_exadecimal_sample

class Security_Group_Data_Generator:

    def get_ip_permissions(self, num: int):
        
        ip_permissions = []

        for x in range(num):
            ip_permissions.append(IpPermissionGenerator.get_ip_permission())

        return ip_permissions


    def get_group_id(self):
        return "sg-" + get_exadecimal_sample(17)


    def get_tags(self, num: int):

        tags = []

        for x in range(num):
            tags.append(TagGenerator.get_tag())

        return tags


    def get_vpc_id(self) -> str:
        return "vpc-" + get_exadecimal_sample(8)

