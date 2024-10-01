import uuid

from sqlmodel import Field, SQLModel, JSON, Column


class User(SQLModel):
    id: uuid.UUID
    is_superuser: bool


class DeviceBase(SQLModel):
    type_id: uuid.UUID
    house_id: uuid.UUID
    serial_number: str = Field(min_length=1, max_length=255)
    name: str = Field(min_length=1, max_length=255)
    description: str | None = Field(default=None, max_length=255)
    connection_data: str = Field(min_length=1, max_length=255)


class DeviceTypeBase(SQLModel):
    type_name: str = Field(min_length=1, max_length=255)
    description: str | None = Field(default=None, max_length=255)


class DeviceConfigurationBase(SQLModel):
    configuration: dict


class DeviceCreate(DeviceBase):
    pass


class DeviceTypeCreate(DeviceTypeBase):
    pass


class DeviceUpdate(DeviceBase):
    type_id: uuid.UUID | None = Field(default=None)  # type: ignore
    house_id: uuid.UUID | None = Field(default=None)  # type: ignore
    serial_number: str | None = Field(default=None, min_length=1, max_length=255)  # type: ignore
    name: str | None = Field(default=None, min_length=1, max_length=255)  # type: ignore
    description: str | None = Field(default=None, min_length=1, max_length=255)  # type: ignore
    connection_data: str | None = Field(default=None, min_length=1, max_length=255)  # type: ignore


class DeviceTypeUpdate(DeviceBase):
    type_name: str | None = Field(default=None, min_length=1, max_length=255)  # type: ignore


class DeviceConfigurationUpdate(DeviceConfigurationBase):
    configuration: dict


class DeviceStatusUpdate(SQLModel):
    status: str


class Device(DeviceBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    type_id: uuid.UUID = Field(foreign_key="devicetype.id", nullable=False, ondelete="CASCADE")
    user_id: uuid.UUID


class DeviceType(DeviceTypeBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)


class DeviceConfiguration(DeviceConfigurationBase, table=True):
    device_id: uuid.UUID = Field(foreign_key="device.id", nullable=False, ondelete="CASCADE", primary_key=True)
    configuration: dict = Field(sa_column=Column(JSON))


class DevicePublic(DeviceBase):
    id: uuid.UUID


class DevicesPublic(SQLModel):
    data: list[DevicePublic]
    count: int


class DeviceTypePublic(DeviceTypeBase):
    id: uuid.UUID


class DevicesTypePublic(SQLModel):
    data: list[DeviceTypePublic]
    count: int


class DeviceConfigurationPublic(DeviceConfigurationBase):
    device_id: uuid.UUID


class Message(SQLModel):
    message: str


class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"


class TokenPayload(SQLModel):
    id: uuid.UUID
    is_superuser: bool
