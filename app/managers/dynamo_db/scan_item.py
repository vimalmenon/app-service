from app.managers.dynamo_db.base_db import BaseDB


class ScanItem(BaseDB):

    def __init__(self):
        super().__init__()

    def execute(self):
        return self.table.scan(
            TableName="Application",
            # ExpressionAttributeValues={
            #     ":appKey": "APP#KM#NOTE",
            # },
            # KeyConditionExpression="appKey = :appKey",
        )
