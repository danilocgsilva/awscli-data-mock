from awsclimock.Security_Group_Data_Generator import Security_Group_Data_Generator
from awsclimock.AWS_General_Entities_Mocker import AWS_General_Entities_Mocker
from awsclimock.helpers import get_exadecimal_sample, get_mac_address, get_mocked_network_interface_data

def get_mocked_security_group_data() -> dict:

    security_group_data_generator = Security_Group_Data_Generator()
    vpc_id = security_group_data_generator.get_vpc_id()

    data = {
        "SecurityGroups": [
            {
                "Description": "Santa Fé",
                "GroupName": "santa-fe",
                "IpPermissions": security_group_data_generator.get_ip_permissions(0),
                "OwnerId": AWS_General_Entities_Mocker().get_owner_id(),
                "GroupId": security_group_data_generator.get_group_id(),
                "IpPermissionEgress": security_group_data_generator.get_ip_permissions(1),
                "Tags": security_group_data_generator.get_tags(1),
                "VpcId": vpc_id
            }
        ]
    }

    return data


def get_mocked_ec2_data() -> dict:

    aws_general_entities_mocker = AWS_General_Entities_Mocker()

    owner_id = aws_general_entities_mocker.get_owner_id()
    private_ip = aws_general_entities_mocker.get_ip()
    subnet_id = "subnet-" + get_exadecimal_sample(8)
    vpc_id = "vpc-" + get_exadecimal_sample(8)
    security_group_id = "sg-" + get_exadecimal_sample(17)

    data = {
        "Reservations": [
            {
                "Groups": [],
                "Instances": [
                    {
                        "AmiLaunchIndex": 0,
                        "ImageId": "ami-" + get_exadecimal_sample(17),
                        "InstanceId": "i-" + get_exadecimal_sample(17),
                        "InstanceType": "t2.micro",
                        "KeyName": "my-secret-key",
                        "LaunchTime": "2018-01-05T09:05:52.000Z",
                        "Monitoring": {
                            "State": "disabled"
                        },
                        "Placement": {
                            "AvailabilityZone": "us-east-1b",
                            "GroupName": "",
                            "Tenancy": "default"
                        },
                        "Platform": "windows",
                        "PrivateDnsName": "ip-" + private_ip.replace(".", "-") + ".ec2.internal",
                        "PrivateIpAddress": private_ip,
                        "ProductCodes": [],
                        "PublicDnsName": "",
                        "State": {
                            "Code": 80,
                            "Name": "stopped"
                        },
                        "StateTransitionReason": "User initiated (2018-12-11 11:13:25 GMT)",
                        "SubnetId": subnet_id,
                        "VpcId": vpc_id,
                        "Architecture": "x86_64",
                        "BlockDeviceMappings": [
                            {
                                "DeviceName": "/dev/sda1",
                                "Ebs": {
                                    "AttachTime": "2018-10-18T00:44:49.000Z",
                                    "DeleteOnTermination": True,
                                    "Status": "attached",
                                    "VolumeId": "vol-" + get_exadecimal_sample(17)
                                }
                            }
                        ],
                        "ClientToken": "",
                        "EbsOptimized": False,
                        "EnaSupport": True,
                        "Hypervisor": "xen",
                        "NetworkInterfaces": [
                            get_mocked_network_interface_data(
                                security_group_id, 
                                owner_id, 
                                private_ip,
                                subnet_id,
                                vpc_id
                            )
                        ],
                        "RootDeviceName": "/dev/sda1",
                        "RootDeviceType": "ebs",
                        "SecurityGroups": [
                            {
                                "GroupName": "default",
                                "GroupId": security_group_id
                            }
                        ],
                        "SourceDestCheck": True,
                            "StateReason": {
                            "Code": "Client.UserInitiatedShutdown",
                            "Message": "Client.UserInitiatedShutdown: User initiated shutdown"
                        },
                        "Tags": [
                            {
                                "Key": "Description",
                                "Value": "General porpouse machine"
                            },
                        ],
                        "VirtualizationType": "hvm",
                        "CpuOptions": {
                            "CoreCount": 1,
                            "ThreadsPerCore": 1
                        },
                        "CapacityReservationSpecification": {
                            "CapacityReservationPreference": "open"
                        },
                        "HibernationOptions": {
                            "Configured": False
                        },
                        "MetadataOptions": {
                            "State": "applied",
                            "HttpTokens": "optional",
                            "HttpPutResponseHopLimit": 1,
                            "HttpEndpoint": "enabled"
                        }
                    }
                ],
                "OwnerId": owner_id,
                "ReservationId": "r-" + get_exadecimal_sample(17)
            }
        ]
    }

    return data


def get_mocked_regions() -> dict:
    return {
        "Regions": [
            {
                "Endpoint": "ec2.eu-north-1.amazonaws.com",
                "RegionName": "eu-north-1",
                "OptInStatus": "opt-in-not-required"
            },
            {
                "Endpoint": "ec2.ap-south-1.amazonaws.com",
                "RegionName": "ap-south-1",
                "OptInStatus": "opt-in-not-required"
            },
            {
                "Endpoint": "ec2.eu-west-3.amazonaws.com",
                "RegionName": "eu-west-3",
                "OptInStatus": "opt-in-not-required"
            },
            {
                "Endpoint": "ec2.eu-west-2.amazonaws.com",
                "RegionName": "eu-west-2",
                "OptInStatus": "opt-in-not-required"
            },
            {
                "Endpoint": "ec2.eu-west-1.amazonaws.com",
                "RegionName": "eu-west-1",
                "OptInStatus": "opt-in-not-required"
            },
            {
                "Endpoint": "ec2.ap-northeast-2.amazonaws.com",
                "RegionName": "ap-northeast-2",
                "OptInStatus": "opt-in-not-required"
            },
            {
                "Endpoint": "ec2.ap-northeast-1.amazonaws.com",
                "RegionName": "ap-northeast-1",
                "OptInStatus": "opt-in-not-required"
            },
            {
                "Endpoint": "ec2.sa-east-1.amazonaws.com",
                "RegionName": "sa-east-1",
                "OptInStatus": "opt-in-not-required"
            },
            {
                "Endpoint": "ec2.ca-central-1.amazonaws.com",
                "RegionName": "ca-central-1",
                "OptInStatus": "opt-in-not-required"
            },
            {
                "Endpoint": "ec2.ap-southeast-1.amazonaws.com",
                "RegionName": "ap-southeast-1",
                "OptInStatus": "opt-in-not-required"
            },
            {
                "Endpoint": "ec2.ap-southeast-2.amazonaws.com",
                "RegionName": "ap-southeast-2",
                "OptInStatus": "opt-in-not-required"
            },
            {
                "Endpoint": "ec2.eu-central-1.amazonaws.com",
                "RegionName": "eu-central-1",
                "OptInStatus": "opt-in-not-required"
            },
            {
                "Endpoint": "ec2.us-east-1.amazonaws.com",
                "RegionName": "us-east-1",
                "OptInStatus": "opt-in-not-required"
            },
            {
                "Endpoint": "ec2.us-east-2.amazonaws.com",
                "RegionName": "us-east-2",
                "OptInStatus": "opt-in-not-required"
            },
            {
                "Endpoint": "ec2.us-west-1.amazonaws.com",
                "RegionName": "us-west-1",
                "OptInStatus": "opt-in-not-required"
            },
            {
                "Endpoint": "ec2.us-west-2.amazonaws.com",
                "RegionName": "us-west-2",
                "OptInStatus": "opt-in-not-required"
            }
        ]
    }
