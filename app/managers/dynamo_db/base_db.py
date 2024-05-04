"""
This is base db
"""

from abc import ABC, abstractmethod
import boto3


class BaseDB(ABC):
    """
    This is base db
    """

    def __init__(self, table):
        self.table = table if table else boto3.resource("dynamodb").Table("test")

    @abstractmethod
    def execute(self):

        pass
