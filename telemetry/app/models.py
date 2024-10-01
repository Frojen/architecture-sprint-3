import uuid
from datetime import datetime

from sqlmodel import Field, SQLModel, JSON, Column


class User(SQLModel):
    id: uuid.UUID
    is_superuser: bool


class SensorBase(SQLModel):
    device_id: uuid.UUID
    name: str = Field(min_length=1, max_length=255)
    description: str | None = Field(default=None, max_length=255)
    connection_data: str = Field(min_length=1, max_length=255)


class TelemetryBase(SQLModel):
    sensor_id: uuid.UUID
    timestamp: datetime
    data: dict = Field(sa_column=Column(JSON))


class SensorCreate(SensorBase):
    pass


class SensorUpdate(SensorBase):
    device_id: uuid.UUID | None = Field(default=None)  # type: ignore
    name: str | None = Field(default=None, min_length=1, max_length=255)  # type: ignore
    description: str | None = Field(default=None, min_length=1, max_length=255)  # type: ignore
    connection_data: str | None = Field(default=None, min_length=1, max_length=255)  # type: ignore


class TelemetryUpdate(SQLModel):
    sensor_id: uuid.UUID
    data: dict


class Sensor(SensorBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID


class Telemetry(TelemetryBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    sensor_id: uuid.UUID = Field(foreign_key="sensor.id", nullable=False, ondelete="CASCADE")


class SensorPublic(SensorBase):
    id: uuid.UUID


class SensorsPublic(SQLModel):
    data: list[SensorPublic]
    count: int


class TelemetryPublic(SQLModel):
    data: list[TelemetryBase]


class Message(SQLModel):
    message: str


class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"


class TokenPayload(SQLModel):
    id: uuid.UUID
    is_superuser: bool
