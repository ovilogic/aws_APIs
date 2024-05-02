import boto3
import sys
import logging
from botocore.exceptions import ClientError

if len(sys.argv) > 1:
	
	bucket_name_cmdLine = sys.argv[1]
	region_cmdLine = sys.argv[2]



def create_bucket(bucket_name, region=None):
	"""Create an S3 bucket in a specified region"""
	try:
		if region is None:
			s3_client = boto3.client('s3')
			s3_client.create_bucket(Bucket=bucket_name)
		else:
			s3_client = boto3.client('s3', region_name=region)
			location = {'LocationConstraint': region}
			s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)

	except ClientError as e:
		logging.error(e)
		return False
	print('done')
	return True


create_bucket(bucket_name_cmdLine, region=region_cmdLine)

