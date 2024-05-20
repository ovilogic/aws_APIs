'''
ex4.6 Remove the RDS instance and the security group.
'''

import boto3
import json

from private_variables import rds_identifier, sg_name, sg_id_number

rds_client = boto3.client('rds')

response = rds_client.delete_db_instance(
    DBInstanceIdentifier=rds_identifier,
    SkipFinalSnapshot=True)

print('RDS Instance is being terminated... Make take a few minutes.')

waiter = rds_client.get_waiter('db_instance_deleted')
waiter.wait(DBInstanceIdentifier=rds_identifier)

# Now on to the security group. As it's a dependency.
print('RDS db has been deleted. Removing the security group now.')

ec2_client = boto3.client('ec2')

response = ec2_client.describe_security_groups(
    GroupNames=[
        sg_name
    ]
)

sg_id_number = json.dumps(response['SecurityGroups'][0]['GroupId'])
sg_id_number = sg_id_number.replace('"', '')

response = ec2_client.delete_security_group(
    GroupId=sg_id_number
)

print('Cleanup now complete. Enjoy lunch, Ovi!')