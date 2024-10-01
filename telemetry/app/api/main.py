from fastapi import APIRouter

from app.api.routes import sensors, telemetry, monolith

api_router = APIRouter()
api_router.include_router(sensors.router, prefix="/sensors", tags=["sensors"])
api_router.include_router(telemetry.router, prefix="/telemetry", tags=["telemetry"])

api_monolith_router = APIRouter()
api_monolith_router.include_router(monolith.router, prefix="/telemetry", tags=["monolith"])
