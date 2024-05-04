"""
This is file for get item
"""

from app.managers.dynamo_db.base_db import BaseDB


class GetItem(BaseDB):
    """
    This is get item
    """

    def __init__(self, table):
        super().__init__(table)


    def execute(self):
        return self.table
