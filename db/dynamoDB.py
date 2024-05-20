import boto3
import json
import datetime

dynamodb_resource = boto3.resource('dynamodb')

table = dynamodb_resource.create_table(
    TableName='Users',
    KeySchema=[
        {
            'AttributeName': 'user_id',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'user_email',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'user_id',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'user_email',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

print("the DynamoDB table is being created. This may take a few minutes...")
table.meta.client.get_waiter('table_exists').wait(TableName='Users')
print('Table is ready!')