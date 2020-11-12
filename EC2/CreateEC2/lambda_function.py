import os
import boto3

# AMI = os.environ['AMI']
# INSTANCE_TYPE = os.environ['INSTANCE_TYPE']
# KEY_NAME = os.environ['KEY_NAME']
# SUBNET_ID = os.environ['SUBNET_ID']

ec2 = boto3.resource('ec2')


def lambda_handler(event, context):

    instance = ec2.create_instances(
        ImageId="ami-0039653380f1f0b2b",
        InstanceType="t2.micro",
        # KeyName=KEY_NAME,
        SubnetId="subnet-0cb7a572588a09009",
        MaxCount=1,
        MinCount=1
    )

    print("New instance created:", instance[0].id)

