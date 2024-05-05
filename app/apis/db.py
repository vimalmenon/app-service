"""
This is api root file
"""

from fastapi import APIRouter

db_router = APIRouter()


@db_router.get("/", tags=["root"])
async def root():
    """
    This is Root URL
    """
    return "test"
