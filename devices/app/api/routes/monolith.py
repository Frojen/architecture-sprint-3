import uuid
from typing import Any

from fastapi import APIRouter, HTTPException

from app.api.deps import SessionDep
from app.models import DeviceConfigurationPublic, Device, DeviceStatusUpdate
from app.services.devices import set_device_configuration


router = APIRouter()


@router.put("/{device_id}/status", response_model=DeviceConfigurationPublic)
def update_status(
    *,
    session: SessionDep,
    device_id: uuid.UUID,
    device_status_in: DeviceStatusUpdate,
) -> Any:
    """
    Update a device configuration.
    """
    device = session.get(Device, device_id)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    configuration = set_device_configuration(session, device=device, configuration=device_status_in.model_dump())
    return DeviceConfigurationPublic(device_id=device.id, configuration=configuration)
