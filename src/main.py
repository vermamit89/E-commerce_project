from fastapi import FastAPI
from .routes import common
from .models import database

app=FastAPI()

database.base.metadata.create_all(database.engine)

app.include_router(common.router)
