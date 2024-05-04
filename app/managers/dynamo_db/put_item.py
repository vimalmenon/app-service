"""
This is file for put item to database
"""

from app.managers.dynamo_db.base_db import BaseDB


class PutItem(BaseDB):
    """
    This is put item
    """

    def __init__(self, table):
        super().__init__(table)



    def execute(self):
        return self.table
