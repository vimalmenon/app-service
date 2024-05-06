"""
This is file for delete item
"""

from app.managers.dynamo_db.base_db import BaseDB


class DeleteItem(BaseDB):
    """
    This is delete item
    """

    def __init__(self):
        super().__init__()

    def execute(self):
        return self.table.delete_item(
            TableName="Application",
            Key={
                "appKey": "Pri Key",
                "sortKey": "Sec Key",
            },
        )
