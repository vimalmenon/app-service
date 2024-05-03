from app.apis.root import root_router
from fastapi import FastAPI

app = FastAPI()
app.include_router(root_router, prefix="/user")
