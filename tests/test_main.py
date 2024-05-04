"""
This is main test
"""

import pytest

from app.services.root_service import RootService
from app.managers.dynamo_db.delete_item import DeleteItem


# pylint: disable=redefined-outer-name
@pytest.fixture(name="mock_response")
def mock_response():
    """Requests.get() mocked to return {'mock_key':'mock_response'}."""
    return "table"


def test_main():
    """
    This is main test
    """
    result = RootService().data()
    assert result[0]["username"] == "Rick"
    assert result[1]["username"] == "Morty"


def test_delete_item(mock_response):
    """
    This is delete item
    """
    print(DeleteItem(table=mock_response).execute())
