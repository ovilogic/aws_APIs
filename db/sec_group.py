'''
ex4.1 Create a database for the Database Tier on RDS.
'''

import boto3
import json
import datetime

from private_variables import sg_name, sg_description, my_ip_cidr

# Creating the EC2 client to create the security group for the database.
ec2_client = boto3.client('ec2')

# First, we need to create the security group.
response = ec2_client.create_security_group(
    Description=sg_description,
    GroupName=sg_name
)

print(json.dumps(response, indent=2, sort_keys=True))

# Adding a rule to the security group.
response = ec2_client.authorize_security_group_ingress(
    CidrIp=my_ip_cidr,
    FromPort=3306,
    GroupName=sg_name,
    ToPort=3306,
    IpProtocol='tcp'
)

print("Security group should be created! Verify this in AWS console.")