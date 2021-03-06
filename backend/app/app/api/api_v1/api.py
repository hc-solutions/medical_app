from fastapi import APIRouter

from app.api.api_v1.endpoints import (
    medical_items,
    items,
    login,
    users,
    utils,
    patients,
    procedures,
    diseases,
)

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(patients.router, prefix="/patients", tags=["patients"])
api_router.include_router(procedures.router, prefix="/procedures", tags=["procedures"])
api_router.include_router(
    medical_items.router, prefix="/medical_items", tags=["medical_items"]
)
api_router.include_router(diseases.router, prefix="/diseases", tags=["diseases"])
