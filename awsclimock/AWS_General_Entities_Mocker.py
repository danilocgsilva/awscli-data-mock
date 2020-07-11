import math
from random import random
from awsclimock.helpers import random_until_255

class AWS_General_Entities_Mocker:

    def get_owner_id(self):

        owner_id = ""
        for x in range(12):
            owner_id += str(math.ceil(random() * 10))

        return owner_id


    def get_ip(self):
        return "-".join([random_until_255(), random_until_255(), random_until_255(), random_until_255()])