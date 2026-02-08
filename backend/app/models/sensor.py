from pydantic import BaseModel
from datetime import datetime

class SensorReading(BaseModel):
    device_id: str
    sensor_type: str
    value: float
    timestamp: datetime = datetime.utcnow()
