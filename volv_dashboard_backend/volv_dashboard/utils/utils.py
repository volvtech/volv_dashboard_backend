from django.conf import settings
from botocore.config import Config

import logging
import os
import boto3


def upload_doc_to_s3_bucket(doc_path, bucket, key):
    logging.info(f"#volv_dashboard #utils #utils.py upload_doc_to_s3_bucket doc_path: {doc_path} bucket: {bucket}"
                 f" key: {key}")
    if os.path.exists(doc_path):
        s3_client = boto3.client('s3',
                                 aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                                 aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                                 region_name=settings.AWS_S3_REGION_NAME,
                                 config=Config(signature_version='s3v4'),
                                 )
        extra_args = {'ACL': 'private'}
        s3_client.upload_file(doc_path, bucket, ExtraArgs=extra_args)
        region = s3_client.get_bucket_location(Bucket=bucket)['LocationConstraint']
        url = f'https://{bucket}.s3.{region}.amazonaws.com./{key}'
        return url
    else:
        return None
