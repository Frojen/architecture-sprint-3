import requests

from sqlmodel import Session

from app.models import Device, DeviceConfiguration


class RequestError(Exception):
    pass


def set_device_configuration(session: Session, device: Device, configuration: dict) -> dict:
    response = requests.post(device.connection_data, json=configuration)
    if response.status_code != 200:
        raise RequestError
    device_configuration = session.get(DeviceConfiguration, device.id)
    if not device_configuration:
        new_device_configuration = DeviceConfiguration(device_id=device.id, configuration=response.json())
        session.add(new_device_configuration)
    else:
        device_configuration.configuration = response.json()
    session.commit()
    return response.json()


def get_device_configuration(session: Session, device: Device) -> dict:
    response = requests.get(device.connection_data)
    if response.status_code != 200:
        raise RequestError
    device_configuration = session.get(DeviceConfiguration, device.id)
    if not device_configuration:
        new_device_configuration = DeviceConfiguration(device_id=device.id, configuration=response.json())
        session.add(new_device_configuration)
    else:
        device_configuration.configuration = response.json()
    session.commit()
    return response.json()
