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
        return self.table
