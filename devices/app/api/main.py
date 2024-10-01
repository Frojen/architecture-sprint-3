from fastapi import APIRouter

from app.api.routes import devices, device_types, monolith

api_router = APIRouter()
api_router.include_router(devices.router, prefix="/devices", tags=["devices"])
api_router.include_router(device_types.router, prefix="/device_types", tags=["device_types"])

api_monolith_router = APIRouter()
api_monolith_router.include_router(monolith.router, prefix="/devices", tags=["monolith"])
