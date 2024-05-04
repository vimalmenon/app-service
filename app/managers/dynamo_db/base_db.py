"""
This is base db
"""

from abc import ABC, abstractmethod
import boto3
from botocore.config import Config


dynamodb = boto3.resource("dynamodb")


class BaseDB(ABC):
    """
    This is base db
    """

    def __init__(self, **kwargs):
        self.table = (
            kwargs.get("table")
            if kwargs.get("table")
            else dynamodb.Table("Application")
        )

    @abstractmethod
    def execute(self):

        pass
