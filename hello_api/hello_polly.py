#! python
import logging
import boto3

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')

polly = boto3.client("polly")
                     # region_name='eu-north-1',
                     # aws_access_key_id='xxxxxxxxxxxxxxxxxx',
                     # aws_secret_access_key='xxxxxxxxxxxxxxxxxxxxxx')

result = polly.synthesize_speech(Text='Hello World!',
                                 OutputFormat='mp3',
                                 VoiceId='Aditi')

# Save the audio from response
audio = result['AudioStream'].read()
with open("helloworld.mp3", "wb") as f:
    f.write(audio)