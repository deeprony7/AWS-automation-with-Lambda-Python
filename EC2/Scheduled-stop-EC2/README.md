# Scheduled stopping of EC2 instances

### Lambda Function

Ensure to set the Lambda function timeout high enough (i.e. 1 minute) so that it can iterate through every instance in every region.

### CloudWatch Event Rule

CloudWatch Event acts as the scheduler

Cron expression: `0 23 ? * MON-FRI *`

6:00pm EST (UTC-5) == 11:00pm (23:00) UTC  

Blog Article - https://docs.google.com/document/d/1R62_DxjVg4eo2hBYwwW2ixG3FD-m7-1BCcrwzQi0b58/edit?usp=sharing
