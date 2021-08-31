from decimal import Decimal
import json

import boto3


class DecimalEncoder(json.JSONEncoder):
    """Helper class to convert a DynamoDB item to JSON"""

    def default(self, o):
        if isinstance(o, Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


dynamodb = boto3.resource("dynamodb")

table = dynamodb.Table("Movies")

title = "The Big New Movie"
year = 2015

response = table.update_item(
    Key={"year": year, "title": title},
    UpdateExpression="set info.rating= :r, info.plot=:p, info.actors= :a",
    ExpressionAttributeValues={
        ":r": Decimal(5.5),
        ":p": "Everythong happend all at onece",
        ":a": ["Larry", "Moe", "Curly"],
    },
    ReturnValues="UPDATED_NEW",
)

print("UpdateItem succeeded:")
print(json.dumps(response, indent=4, cls=DecimalEncoder))
