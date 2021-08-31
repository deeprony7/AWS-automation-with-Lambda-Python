"""Multipart transfers occur when the file size exceeds the value of the multipart_threshold attribute."""

"""
The following example configures an upload_file transfer to be multipart if the file size is larger than the threshold specified in the TransferConfig object.
"""


# Set the desired multipart threshold value (5GB)
import boto3
from boto3.s3.transfer import TransferConfig

GB = 1024 ** 3
config = TransferConfig(multipart_threshold=5 * GB)

# Perform the transfer
s3 = boto3.client("s3")
s3.upload_file("FILE_NAME", "BUCKET_NAME", "OBJECT_NAME", Config=config)
