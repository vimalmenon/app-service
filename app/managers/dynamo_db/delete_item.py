"""
This is file for delete item
"""

from app.managers.dynamo_db.base_db import BaseDB


class DeleteItem(BaseDB):
    """
    This is delete item
    """

    def __init__(self, table):
        super().__init__(table)

    def execute(self):
        return self.table.get_item(
            Key={
                "appKey": "APP#KM#FOLDER",
                "sortKey": "note#fedb931d-5937-4508-a50d-47d68b106414",
            }
        )
