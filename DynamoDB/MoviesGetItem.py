from decimal import Decimal
import json

import boto3
from boto3.dynamodb.conditions import Attr, Key
from botocore.exceptions import ClientError


class DecimalEncoder(json.JSONEncoder):
    """Helper class to convert dict to JSON"""

    def default(self, arg):
        if isinstance(arg, Decimal):
            if arg % 1 > 0:
                return float(arg)
            else:
                return int(arg)
        return super(DecimalEncoder, self).default(arg)


dynamodb = boto3.resource("dynamodb")

table = dynamodb.Table("Movies")

title = "The Big New Movie"
year = 2015

try:
    response = table.get_item(Key={"year": year, "title": title})
except ClientError as e:
    print(e.reponse["Error"]["Message"])
else:
    item = response["Item"]
    print("GetItem Succeeded!\n")
    print(json.dumps(item, indent=4, cls=DecimalEncoder))
