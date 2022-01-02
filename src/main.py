from fastapi import FastAPI
from .routes import common

app=FastAPI()

app.include_router(common.router)
