'''
ex4.8 Add Users to DynamoDB table.
'''

import boto3
import json
import uuid


# Createe a DynamoDB resource.
dynamodb_resource = boto3.resource('dynamodb')
table = dynamodb_resource.Table('Users')

# Write a record to DynamoDB
response = table.put_item(
    Item={
        'user_id': '1234-5678',
        'user_email': 'some@dome.com',
        'user_fname': 'Sam',
        'user_lname': 'Romertson'
    }
)

# Printing the Json response. You should see a 200 status code.
print(json.dumps(response, indent=2, sort_keys=True))