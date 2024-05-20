'''
ex4.11 Remove the DynamoDB table
'''


import boto3
import json

dynamodb_client = boto3.client('dynamodb')

# Delete the table.
response = dynamodb_client.delete_table(TableName='Users')
print(json.dumps(response, indent=2, sort_keys=True))

