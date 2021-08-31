"""
The maximum number of concurrent S3 API transfer operations can be tuned to adjust for the connection speed. Set the max_concurrency attribute to increase or decrease bandwidth usage.

The attribute's default setting is 10. To reduce bandwidth usage, reduce the value; to increase usage, increase it.
"""

import boto3
from boto3.s3.transfer import TransferConfig


# To consume less downstream bandwidth, decrease the maximum concurrency
config = TransferConfig(max_concurrency=5)

# Download an S3 object
s3 = boto3.client('s3')
s3.download_file('BUCKET_NAME', 'OBJECT_NAME', 'FILE_NAME', Config=config)