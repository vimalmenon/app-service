"""
This is main test
"""
from app.services.root_service import RootService


def test_main():
    """
    This is main test
    """
    result = RootService().data()
    assert result[0]["username"] == "Rick"
    assert result[1]["username"] == "Morty"
