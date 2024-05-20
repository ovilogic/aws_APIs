'''
ex4.9 Look Up a User in the DB table.
'''

import boto3
from boto3.dynamodb.conditions import Key
import json

dynamodb_resource = boto3.resource('dynamodb')
table = dynamodb_resource.Table('Users')

response = table.query(
    KeyConditionExpression=Key('user_id').eq('1234-5678')
)

# Print the data out.
print(json.dumps(response['Items'], indent=2, sort_keys=True))