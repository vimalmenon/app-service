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
        return self.table.get_item(
            TableName="Application",
            Key={
                "appKey": "APP#KM#FOLDERS_FILE",
                "sortKey": "03461138-2607-41ef-ae10-2cceb0ee2543#396d8acb-2bc0-4e72-a17c-79746902720c.JPG",
            },
            # ExpressionAttributeValues={
            #     ":appKey": "APP#KM#NOTE",
            # },
            # KeyConditionExpression="appKey = :appKey",
        )
