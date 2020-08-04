import sys
import json
from awsclimock.helpers import get_command_to_mock
from awsapimock.Security_Group_Data_Generator \
    import Security_Group_Data_Generator
from awsapimock.Instance_Data_Generator \
    import Instance_Data_Generator
from awsapimock.Regions_Data_Generator \
    import Regions_Data_Generator
from awsapimock.RDS_Data_Generator \
    import RDS_Data_Generator

def main():
    aws_command = get_command_to_mock()

    data = None

    if aws_command == 'describe-security-groups':
        data = Security_Group_Data_Generator().generate()
    elif aws_command == 'describe-instances':
        data = Instance_Data_Generator().generate()
    elif aws_command == 'describe-regions':
        data = Regions_Data_Generator().generate()
    elif aws_command == 'describe-db-instances':
        data = RDS_Data_Generator().generate()
    
    if data == None:
        print('I dont know this command yet!')
        exit()

    print(json.dumps(data))


if __name__ == '__main__':
    main()
