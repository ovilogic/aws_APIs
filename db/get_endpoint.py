'''
ex4.3 Obtain the Endpoint value for the RDS MariaDB instance just created.
'''

import boto3
import json
import datetime

from private_variables import rds_identifier


# Helper function in case you wanna print raw JSON.
def date_time_converter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()


# Create the client for RDS
rds_client = boto3.client('rds')

print('Fetching the RDS endpoint, Ovi.')
response = rds_client.describe_db_instances(
    DBInstanceIdentifier=rds_identifier
)

rds_endpoint = json.dumps(response['DBInstances'][0]['Endpoint']['Address'])
rds_endpoint = rds_endpoint.replace('"', '')
print('RDS enpoint: ' + rds_endpoint)
