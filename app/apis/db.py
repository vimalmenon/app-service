"""
This is api root file
"""

from fastapi import APIRouter
from app.managers.dynamo_db import ScanItem, QueryItems, GetItem, PutItem

db_router = APIRouter()


@db_router.get("/scan", tags=["db"])
async def scan():
    """
    This is Root URL
    """
    return ScanItem().execute()


@db_router.get("/get_item", tags=["db"])
async def get_item():
    """
    This is Root URL
    """
    return GetItem().execute()


@db_router.get("/query", tags=["db"])
async def get_item():
    """
    This is Root URL
    """
    return QueryItems().execute()


@db_router.get("/put_item", tags=["db"])
async def put_item():
    """
    This is Root URL
    """
    return PutItem().execute()
