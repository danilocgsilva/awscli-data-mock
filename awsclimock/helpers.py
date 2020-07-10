import sys
from awsclimock.Security_Group_Data_Generator import Security_Group_Data_Generator
from awsclimock.AWS_General_Entities_Mocker import AWS_General_Entities_Mocker


def get_command_to_mock() -> str:

    try:
        command = sys.argv[1]
    except IndexError:
        command = ask_command()

    return command


def ask_command():
    return input("Which AWS command do you wish to mock? Please, type the command name: ")


def get_mocked_security_group_data() -> dict:

    vpc_id = Security_Group_Data_Generator.get_vpc_id()

    data = {
        "SecurityGroups": [
            {
                "Description": "Santa Fé",
                "GroupName": "santa-fe",
                "IpPermissions": Security_Group_Data_Generator.get_ip_permissions(0),
                "OwnerId": AWS_General_Entities_Mocker().get_owner_id(),
                "GroupId": Security_Group_Data_Generator.get_group_id(),
                "IpPermissionEgress": Security_Group_Data_Generator.get_ip_permissions(1),
                "Tags": Security_Group_Data_Generator.get_tags(1),
                "VpcId": vpc_id
            }
        ]
    }

    return data


def get_mocked_ec2_data() -> dict:

    owner_id = AWS_General_Entities_Mocker().get_owner_id()

    data = {
        "Reservations": [
            {
                "Groups": [],
                "Instances": [],
                "OwnerId": owner_id,
                "ReservationId": "r-" + get_exadecimal_sample(17)
            }
        ]
    }

    return data


    def get_exadecimal_sample(num) -> str:

        possibilities = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

        hexadecimalcode = ""

        for x in range(num):
            hexadecimalcode += possibilities[math.floor(random() * len(possibilities))]

        return hexadecimalcode
