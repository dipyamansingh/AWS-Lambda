import boto3
import json
s3 = boto3.resource('s3')


def lambda_handler(event, context):
    bucket = s3.Bucket('lambdas3test01')
    dest_bucket = s3.Bucket('lambdas3test02')
    print(bucket)
    print(dest_bucket)

    for obj in bucket.objects.all():
        dest_key = obj.key
        print(dest_key)
        s3.Object(dest_bucket.name, dest_key).copy_from(CopySource = {'Bucket': obj.bucket_name, 'Key': obj.key})
    
