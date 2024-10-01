from datetime import datetime
from http import HTTPStatus
from typing import Any

from fastapi import APIRouter, HTTPException, Response

from app.api.deps import SessionDep
from app.models import Telemetry, TelemetryUpdate, Sensor


router = APIRouter()


@router.post("/", response_class=Response, status_code=HTTPStatus.NO_CONTENT)
def update_telemetry(
    *,
    session: SessionDep,
    telemetry_data: TelemetryUpdate,
):
    """
    Update a telemetry data.
    """
    sensor = session.get(Sensor, telemetry_data.sensor_id)
    if not sensor:
        raise HTTPException(status_code=404, detail="Sensor not found")
    telemetry = Telemetry(sensor_id=telemetry_data.sensor_id, timestamp=datetime.now(), data=telemetry_data.data)
    session.add(telemetry)
    session.commit()
