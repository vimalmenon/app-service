"""
This is file for put item to database
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/put_item.html#
"""

from app.managers.dynamo_db.base_db import BaseDB


class PutItem(BaseDB):
    """
    This is put item
    """

    def __init__(self):
        super().__init__()

    def execute(self):
        return self.table.put_item(
            TableName="Application",
            ReturnConsumedCapacity="INDEXES",
            Item={
                "appKey": "Pri Key",
                "sortKey": "Sec Key",
                "active": True,
            },
            # ExpressionAttributeValues={
            #     ":appKey": "APP#KM#NOTE",
            # },
            # KeyConditionExpression="appKey = :appKey",
        )
