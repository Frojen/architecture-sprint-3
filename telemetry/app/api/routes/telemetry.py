import uuid
from typing import Any

from fastapi import APIRouter, HTTPException
from sqlmodel import select

from app.api.deps import CurrentUser, SessionDep
from app.models import TelemetryPublic, Telemetry, Sensor

router = APIRouter()


@router.get("/{sensor_id}", response_model=TelemetryPublic)
def read_telemetry(session: SessionDep, current_user: CurrentUser, sensor_id: uuid.UUID) -> Any:
    """
    Get telemetry by sensor ID.
    """
    sensor = session.get(Sensor, id)
    if not current_user.is_superuser and (sensor.user_id != current_user.id):
        raise HTTPException(status_code=403, detail="Not enough permissions")
    telemetry = session.exec(select(Telemetry).where(Telemetry.sensor_id == sensor_id)).all()
    return TelemetryPublic(data=telemetry)
