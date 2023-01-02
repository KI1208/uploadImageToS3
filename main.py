import boto3
from dotenv import load_dotenv

load_dotenv()
client = boto3.client(
    's3',
)

# .env
# aws_access_key_id='XXXX'
# aws_secret_access_key='XXXX'
# region_name='XXXX'

filename = 'FAQ_BotTest.docx'
key = 'FAQ_BotTest.docx'
bucket = 'temporary-fmq739thhf8w7597yhf'
client.upload_file(filename, bucket, key, ExtraArgs={'ACL': 'public-read'})

def getObjectURL(bucket, target_object_path):
    bucket_location = client.get_bucket_location(Bucket=bucket)
    return "https://s3-{0}.amazonaws.com/{1}/{2}".format(
        bucket_location['LocationConstraint'],
        bucket,
        target_object_path)


print(getObjectURL(bucket, key))
