import decimal
import json

import boto3
from boto3.dynamodb.conditions import Key


class DecimalEncoder(json.JSONEncoder):
    '''Helper class to convert a DynamoDB item to JSON'''

    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Movies')

filter_expression = Key('year').between(1950, 1960)
projection_expression = '#yr, title, info.rating'
# Expression Attribute Names for Projection Expression only.
expression_attribute_names = {"#yr": "year",}
exclusive_start_key = None

response = table.scan(
	FilterExpression=filter_expression,
	ProjectionExpression=projection_expression,
	ExpressionAttributeNames=expression_attribute_names,
)

for item in response['Items']:
	print(json.dumps(item, cls=DecimalEncoder))

while 'LastEvaluatedKey' in response:
	response = table.scan(
		FilterExpression=filter_expression,
		ProjectionExpression=projection_expression,
		ExpressionAttributeNames=expression_attribute_names,
		ExclusiveStartKey=response['LastEvaluatedKey']
	)

	for item in response['Items']:
		print(json.dumps(item, cls=DecimalEncoder))


