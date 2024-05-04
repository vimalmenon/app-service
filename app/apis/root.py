"""
This is api root file
"""

from fastapi import APIRouter
from app.services import RootService

root_router = APIRouter()


@root_router.get("/", tags=["root"])
async def root():
    """
    This is Root URL
    """
    return RootService().data()
