import logging

from fastapi import FastAPI

from app.api.api_v1.api import api_router
from app.core.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.include_router(api_router, prefix=settings.API_V1_STR)

logger.info(settings.model_dump())


@app.get("/")
async def root():
    return {"message": "Hello World"}
