from fastapi import FastAPI
from .routes import common, products
from .models import database, models

app=FastAPI()

models.base.metadata.create_all(database.engine)

app.include_router(common.router)
app.include_router(products.router)
