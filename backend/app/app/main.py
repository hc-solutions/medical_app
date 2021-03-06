import logging
import os

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.api_v1.api import api_router
from app.core.config import settings

logger = logging.getLogger()

START_ARGS = {}
if os.getenv("SCOPE") == "dev":
    START_ARGS = {
        "title": settings.PROJECT_NAME,
        "openapi_url": f"{settings.API_V1_STR}/openapi.json",
    }
else:
    START_ARGS = {"openapi_url": None, "docs": None, "redoc": None}

app = FastAPI(**START_ARGS)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000)
