"""
This is Root Service file
"""

from app.managers.dynamo_db.get_item import GetItem


class RootService:
    """
    This is Root Service class
    """

    def data(self):
        """
        This is Root URL
        """
        print(GetItem().execute())
        return [{"username": "Rick"}, {"username": "Morty"}]

    def passing(self):
        """
        This is just for passing
        """
        print("passing")
