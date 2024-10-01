import uuid
from typing import Any

from fastapi import APIRouter, HTTPException
from sqlmodel import func, select

from app.api.deps import CurrentUser, SessionDep
from app.models import Message, DeviceTypePublic, DeviceType, DeviceTypeCreate, DeviceTypeUpdate, DevicesTypePublic

router = APIRouter()


@router.get("/", response_model=DevicesTypePublic)
def read_device_types(
    session: SessionDep, skip: int = 0, limit: int = 100
) -> Any:
    """
    Retrieve device types.
    """

    count_statement = select(func.count()).select_from(DeviceType)
    count = session.exec(count_statement).one()
    statement = select(DeviceType).offset(skip).limit(limit)
    device_types = session.exec(statement).all()

    return DevicesTypePublic(data=device_types, count=count)


@router.get("/{id}", response_model=DeviceTypePublic)
def read_device_type(session: SessionDep, id: uuid.UUID) -> Any:
    """
    Get device type by ID.
    """
    device_type = session.get(DeviceType, id)
    if not device_type:
        raise HTTPException(status_code=404, detail="Type not found")
    return device_type


@router.post("/", response_model=DeviceTypePublic)
def create_device_type(
    *, session: SessionDep, device_type_in: DeviceTypeCreate, current_user: CurrentUser
) -> Any:
    """
    Create new device type.
    """
    if not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    device_type = DeviceType.model_validate(device_type_in)
    session.add(device_type)
    session.commit()
    session.refresh(device_type)
    return device_type


@router.put("/{id}", response_model=DeviceTypePublic)
def update_device_type(
    *,
    session: SessionDep,
    id: uuid.UUID,
    device_type_in: DeviceTypeUpdate,
    current_user: CurrentUser
) -> Any:
    """
    Update a device type.
    """
    device_type = session.get(DeviceType, id)
    if not device_type:
        raise HTTPException(status_code=404, detail="Device type not found")
    if not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    update_dict = device_type_in.model_dump(exclude_unset=True)
    device_type.sqlmodel_update(update_dict)
    session.add(device_type)
    session.commit()
    session.refresh(device_type)
    return device_type


@router.delete("/{id}")
def delete_device_type(
    session: SessionDep, id: uuid.UUID, current_user: CurrentUser
) -> Message:
    """
    Delete a device type.
    """
    device_type = session.get(DeviceType, id)
    if not device_type:
        raise HTTPException(status_code=404, detail="Device type not found")
    if not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    session.delete(device_type)
    session.commit()
    return Message(message="device type deleted successfully")
