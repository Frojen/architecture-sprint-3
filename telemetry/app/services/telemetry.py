import concurrent.futures
import logging
from datetime import datetime
from time import sleep

import requests

from sqlmodel import Session, select

from app.core.db import engine
from app.models import Sensor, Telemetry


class RequestError(Exception):
    pass


logger = logging.getLogger(__name__)


class TelemetryCron:
    def __init__(self, session: Session):
        self.session = session

    def init(self):
        self._run()

    def _run(self):
        while True:
            try:
                self.wait_until()
                self.update_telemetry()
            except Exception:
                logger.error("Error in telemetry cron.", exc_info=True, stack_info=True)
                continue

    def get_telemetry_data(self, connection_data: str) -> dict:
        response = requests.get(connection_data)
        if response.status_code != 200:
            logger.error("Sensor not available.", exc_info=True, stack_info=True)
        return response.json()

    def wait_until(self):
        sleep(60)

    def update_telemetry(self):
        sensors = self.session.exec(select(Sensor)).all()
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            future_to = {executor.submit(self.get_telemetry_data, sensor.connection_data): sensor.id for sensor in sensors}
            if not future_to:
                return
            for future in concurrent.futures.as_completed(future_to):
                sensor_id = future_to[future]
                try:
                    data = future.result()
                except Exception:
                    logger.error("Internal errol during get sensor data.", exc_info=True, stack_info=True)
                else:
                    telemetry = Telemetry(sensor_id=sensor_id, timestamp=datetime.now(), data=data)
                    self.session.add(telemetry)
                    self.session.commit()


telemetry_cron = TelemetryCron(Session(engine))
