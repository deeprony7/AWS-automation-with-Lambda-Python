import decimal
import json

import boto3
from boto3.dynamodb.conditions import Key


class DecimalEncoder(json.JSONEncoder):
    """Helper class to convert a DynamoDB item to JSON"""

    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


dynamodb = boto3.resource("dynamodb")

table = dynamodb.Table("Movies")

year = 1970
print(f"Movies from the {year}")

response = table.query(KeyConditionExpression=Key("year").eq(year))

for movie in response["Items"]:
    print(f"{movie['year']} :\t{movie['title']}")
