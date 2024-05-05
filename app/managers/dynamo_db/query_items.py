"""
This is file for query items
"""

from app.managers.dynamo_db.base_db import BaseDB


class QueryItems(BaseDB):
    """
    This is query item
    """

    def __init__(self, table):
        super().__init__(table)

    def execute(self):
        return self.table.query(
            TableName="Application",
            ExpressionAttributeValues={
                ":appKey": "APP#KM#NOTE",
            },
            KeyConditionExpression="appKey = :appKey",
        )
