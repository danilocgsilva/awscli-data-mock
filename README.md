# awscli-data-mock

Mocks AWS cli json responses for testing and privacy porpouses

## Install

1. Navigate to the project root.
2. Write the following command:
```
pip install .
```

## Usage

After installed, just type:

```
awsclimock describe-security-group
```
Then you mock data from security group, in the same format as `aws ec2 describe-security-group`.

You also can mock data for ec2 instances:

```
awsclimock describe-instances
```

You will mock data in the format from the `aws ec2 describe-instances`.

Can mock data from regions:

```
awsclimock describe-regions
```

Will split format as the command `aws ec2 describe-regions`. Here we have not concerns to privacy or sensitive information, so the mocked data is exactly the same as the real command will return, unless some update in the region.
