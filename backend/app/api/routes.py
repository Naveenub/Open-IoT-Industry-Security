from fastapi import APIRouter
from app.models.sensor import SensorReading
from app.services.alert_service import check_alerts
from app.db.database import save_reading, get_latest_readings

router = APIRouter(prefix="/api", tags=["IoT"])

@router.post("/ingest")
def ingest_sensor_data(reading: SensorReading):
    save_reading(reading)
    alerts = check_alerts(reading)
    return {"message": "Data ingested", "alerts": alerts}

@router.get("/sensors")
def fetch_latest():
    return get_latest_readings()

@router.get("/alerts")
def get_alerts():
    return check_alerts(None, fetch_all=True)
