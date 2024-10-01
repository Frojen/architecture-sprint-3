import uuid
from typing import Any

from fastapi import APIRouter, HTTPException
from sqlmodel import func, select

from app.api.deps import CurrentUser, SessionDep
from app.models import Message, DevicesPublic, Device, DevicePublic, DeviceConfigurationPublic, DeviceCreate, \
    DeviceUpdate, DeviceConfigurationUpdate
from app.services.devices import get_device_configuration, set_device_configuration

router = APIRouter()


@router.get("/", response_model=DevicesPublic)
def read_devices(
    session: SessionDep, current_user: CurrentUser, skip: int = 0, limit: int = 100
) -> Any:
    """
    Retrieve devices.
    """

    if current_user.is_superuser:
        count_statement = select(func.count()).select_from(Device)
        count = session.exec(count_statement).one()
        statement = select(Device).offset(skip).limit(limit)
        devices = session.exec(statement).all()
    else:
        count_statement = (
            select(func.count())
            .select_from(Device)
            .where(Device.user_id == current_user.id)
        )
        count = session.exec(count_statement).one()
        statement = (
            select(Device)
            .where(Device.user_id == current_user.id)
            .offset(skip)
            .limit(limit)
        )
        devices = session.exec(statement).all()

    return DevicesPublic(data=devices, count=count)


@router.get("/{id}", response_model=DevicePublic)
def read_device(session: SessionDep, current_user: CurrentUser, id: uuid.UUID) -> Any:
    """
    Get device by ID.
    """
    device = session.get(Device, id)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    if not current_user.is_superuser and (device.user_id != current_user.id):
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return device


@router.get("/{id}/configuration", response_model=DeviceConfigurationPublic)
def read_device_configuration(session: SessionDep, current_user: CurrentUser, id: uuid.UUID) -> Any:
    """
    Get device configuration by ID.
    """
    device = session.get(Device, id)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    if not current_user.is_superuser and (device.user_id != current_user.id):
        raise HTTPException(status_code=403, detail="Not enough permissions")
    configuration = get_device_configuration(session, device=device)
    return DeviceConfigurationPublic(device_id=device.id, configuration=configuration)


@router.post("/", response_model=DevicePublic)
def create_device(
    *, session: SessionDep, current_user: CurrentUser, device_in: DeviceCreate
) -> Any:
    """
    Create new device.
    """
    device = Device.model_validate(device_in, update={"user_id": current_user.id})
    session.add(device)
    session.commit()
    session.refresh(device)
    return device


@router.put("/{id}", response_model=DevicePublic)
def update_device(
    *,
    session: SessionDep,
    current_user: CurrentUser,
    id: uuid.UUID,
    device_in: DeviceUpdate,
) -> Any:
    """
    Update an device.
    """
    device = session.get(Device, id)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    if not current_user.is_superuser and (device.user_id != current_user.id):
        raise HTTPException(status_code=403, detail="Not enough permissions")
    update_dict = device_in.model_dump(exclude_unset=True)
    device.sqlmodel_update(update_dict)
    session.add(device)
    session.commit()
    session.refresh(device)
    return device


@router.put("/{id}/configuration", response_model=DeviceConfigurationPublic)
def update_device(
    *,
    session: SessionDep,
    current_user: CurrentUser,
    device_configuration_in: DeviceConfigurationUpdate,
) -> Any:
    """
    Update a device configuration.
    """
    device = session.get(Device, device_configurtion_in.device_id)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    if not current_user.is_superuser and (device.user_id != current_user.id):
        raise HTTPException(status_code=403, detail="Not enough permissions")
    configuration = set_device_configuration(session, device=device, configuration=device_configuration_in.configuration)
    return DeviceConfigurationPublic(device_id=device.id, configuration=configuration)


@router.delete("/{id}")
def delete_device(
    session: SessionDep, current_user: CurrentUser, id: uuid.UUID
) -> Message:
    """
    Delete an device.
    """
    device = session.get(Device, id)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    if not current_user.is_superuser and (device.user_id != current_user.id):
        raise HTTPException(status_code=403, detail="Not enough permissions")
    session.delete(device)
    session.commit()
    return Message(message="device deleted successfully")
