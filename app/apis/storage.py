from fastapi import APIRouter
from app.services import RootService

storage_router = APIRouter()


@storage_router.get("/get_data", tags=["storage"])
async def get_data():
    """
    This is Root URL
    """
    return QueryItems().execute()


@storage_router.get("/delete_data", tags=["storage"])
async def delete_data():
    """
    This is Root URL
    """
    return QueryItems().execute()


@storage_router.get("/upload_data", tags=["storage"])
async def upload_data():
    """
    This is Root URL
    """
    return QueryItems().execute()
