#! python
import logging
import boto3

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')

s3 = boto3.resource('s3')
bucket = s3.Bucket('ovi-testing-sdk')
bucket.objects.all().delete()
bucket.delete()