'''
ex4.2 Spin up MariaDB database that is hosted on RDS.
'''

import boto3
import json
import datetime

# Helper function for date time conversion, in case you want to print out the raw
# JSON.

def date_time_converter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

from private_variables import sg_name, rds_identifier, db_name, user_name
from private_variables import user_password, admin_email, sg_id_number, rds_endpoint

# We need to get the sec gr id number to use when creating the RDS instance.
ec2_client = boto3.client('ec2')
response = ec2_client.describe_security_groups(
    GroupNames=[
        sg_name
    ]
)

sg_id_number = json.dumps(response['SecurityGroups'][0]['GroupId'])
sg_id_number = sg_id_number.replace('"', '')

# Create the client for RDS.
rds_client = boto3.client('rds')

# Following will create the MariaDB database.

response = rds_client.create_db_instance(
    DBInstanceIdentifier=rds_identifier,
    DBName=db_name,
    DBInstanceClass='db.t3.micro',
    Engine='mariadb',
    MasterUsername=user_name,
    MasterUserPassword=user_password,
    VpcSecurityGroupIds=[
        sg_id_number
    ],
    AllocatedStorage=20,
    Tags=[
        {
            'Key': 'POC-email',
            'Value': admin_email
        },
        {
            'Key': 'Purposer',
            'Value': 'AWS Developer textbook exercise'
        }
    ]
)

# We need to wait until the DB Cluster is up.
print('Creating the thing. That is the RDS instace. Which normally takes several \
minutes')

waiter = rds_client.get_waiter('db_instance_available')
waiter.wait(DBInstanceIdentifier=rds_identifier)

print('Okay, the RDS database is up and running, Ovi.')