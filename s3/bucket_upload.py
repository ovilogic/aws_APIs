''' Program that adds items to the already-created S3 bucket.
First, create the items. 2 in number:
	- one, a text file;
	- second, a file (!?);
'''

# from .upload_to_bucket import upload_file_to_s3
import upload_to_bucket

upload_to_bucket.upload_file_to_s3("upload_text.txt", "ovi-testing-sdk", object_name="ovi_object.txt")
