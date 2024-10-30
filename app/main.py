from contextlib import asynccontextmanager

from fastapi import FastAPI

from carts.views import router as carts_router
from carts.dependencies import connect_to_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    connect_to_db()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(carts_router)
