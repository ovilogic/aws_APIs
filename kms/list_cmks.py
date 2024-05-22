import logging
import boto3
import json
from botocore.exceptions import ClientError

# List the KMS keys by ID

kms_client = boto3.client('kms', region_name='eu-north-1')
try:
    response = kms_client.list_keys()
except ClientError as e:
    logging.error(e)    

print(json.dumps(response, indent=4, sort_keys=True))


