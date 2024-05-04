"""
This is file for get item
"""

from app.managers.dynamo_db.base_db import BaseDB
from boto3.dynamodb.conditions import Key


class GetItem(BaseDB):
    """
    This is get item
    """

    def __init__(self):
        super().__init__()

    def execute(self):
        return self.table.query(
            TableName="Application",
            ExpressionAttributeValues={
                ":appKey": "APP#KM#NOTE",
            },
            KeyConditionExpression="appKey = :appKey",
        )
