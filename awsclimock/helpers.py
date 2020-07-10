import sys
from awsclimock.SecurityGroupDataGenerator import SecurityGroupDataGenerator


def get_command_to_mock() -> str:

    try:
        command = sys.argv[1]
    except IndexError:
        command = ask_command()

    return command


def ask_command():
    return input("Which AWS command do you wish to mock? Please, type the command name: ")


def get_mocked_security_group_data() -> dict:

    vpc_id = SecurityGroupDataGenerator.get_vpc_id()

    data = {
        "SecurityGroups": [
            {
                "Description": "Santa Fé",
                "GroupName": "santa-fe",
                "IpPermissions": SecurityGroupDataGenerator.get_ip_permissions(0),
                "OwnerId": SecurityGroupDataGenerator.get_owner_id(),
                "GroupId": SecurityGroupDataGenerator.get_group_id(),
                "IpPermissionEgress": SecurityGroupDataGenerator.get_ip_permissions(1),
                "Tags": SecurityGroupDataGenerator.get_tags(1),
                "VpcId": vpc_id
            }
        ]
    }

    return data
