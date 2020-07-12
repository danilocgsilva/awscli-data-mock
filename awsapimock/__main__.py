import sys
from awsclimock.helpers import get_command_to_mock
from awsapimock.Commands_Output.Security_Group_Data_Generator \
    import Security_Group_Data_Generator
from awsapimock.Commands_Output.Instance_Data_generator \
    import Instance_Data_generator
from awsapimock.Commands_Output.Regions_Data_Generator \
    import Regions_Data_Generator


def main():
    aws_command = get_command_to_mock()

    if aws_command == 'describe-security-group':
        print(Security_Group_Data_Generator().generate())
    elif aws_command == 'describe-instances':
        print(Instance_Data_generator().generate())
    elif aws_command == 'describe-regions':
        print(Regions_Data_Generator().generate())
    else:
        print('I dont know this command yet!')


if __name__ == '__main__':
    main()
