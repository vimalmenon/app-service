"""
This is main file
"""

from fastapi import FastAPI

from app.apis import root_router


app = FastAPI()
app.include_router(root_router, prefix="/user")
