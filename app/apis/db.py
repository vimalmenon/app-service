"""
API for different operation for Dynamo DB
"""

from fastapi import APIRouter, Request, Query, Depends
from typing import Annotated
from app.managers.dynamo_db import ScanItem, QueryItems, GetItem, PutItem, DeleteItem
from typing import Any, Dict, List, Union

db_router = APIRouter()


@db_router.get("/scan", tags=["db"])
async def scan():
    """
    API Scan Database
    """
    return ScanItem().execute()


@db_router.get("/get_item", tags=["db"])
async def get_item():
    """
    API for get item
    """
    return GetItem().execute()


@db_router.get(
    "/query/{table}",
    tags=["db"],
)
async def get_item(table: str, request: Request):
    """
    API for query
    """
    params = Query(**request.query_params)
    print(params.json_schema_extra)
    return params.json_schema_extra
    # return QueryItems().execute()


@db_router.get("/put_item", tags=["db"])
async def put_item():
    """
    API for put item
    """
    return PutItem().execute()


@db_router.get("/delete_item", tags=["db"])
async def delete_item():
    """
    API for delete item
    """
    return DeleteItem().execute()
