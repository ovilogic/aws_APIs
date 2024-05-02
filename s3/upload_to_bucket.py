import boto3
from botocore.exceptions import ClientError
import logging

def upload_file_to_s3(file_name, bucket, object_name=None):
	""" Upload a file to an S3 bucket 
	:param file_name: file to upload
	:param bucket: bucket to upload to
	:param object_name: S3 object name. If not specified then file_name
is used		
	:return: True if file was uploaded, else False
"""
# If S3 object_name was not specified, use file_name
	if object_name is None:
		object_name = file_name

	# Upload this file
	s3_client = boto3.client('s3', region_name='eu-north-1')
	try:
		response = s3_client.upload_file(file_name, bucket, object_name)
	except ClientError as e:
		logging.error(e)
		return False
	return True
