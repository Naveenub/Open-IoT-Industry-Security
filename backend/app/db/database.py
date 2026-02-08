from typing import List
from app.models.sensor import SensorReading

DATABASE: List[SensorReading] = []

def save_reading(reading: SensorReading):
    DATABASE.append(reading)

def get_latest_readings(limit: int = 20):
    return DATABASE[-limit:]
