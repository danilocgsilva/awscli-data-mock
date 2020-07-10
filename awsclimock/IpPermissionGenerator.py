class IpPermissionGenerator:

    def get_ip_permission():
        return {
            "IpProtocol": "-1",
            "IpRanges": [
                {
                    "CidrIp": "0.0.0.0/0"
                }
            ],
            "Ipv6Ranges": [],
            "PrefixListIds": [],
            "UserIdGroupPairs": []
        }        
