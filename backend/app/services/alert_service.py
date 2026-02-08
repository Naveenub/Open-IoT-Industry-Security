from app.core.thresholds import THRESHOLDS
from app.models.sensor import SensorReading

ALERT_LOG = []

def check_alerts(reading: SensorReading | None, fetch_all: bool = False):
    if fetch_all:
        return ALERT_LOG

    alerts = []
    rules = THRESHOLDS.get(reading.sensor_type)

    if not rules:
        return []

    if "critical" in rules and reading.value >= rules["critical"]:
        alert = {
            "level": "CRITICAL",
            "sensor": reading.sensor_type,
            "value": reading.value,
            "device": reading.device_id
        }
        ALERT_LOG.append(alert)
        alerts.append(alert)

    elif "warning" in rules and reading.value >= rules["warning"]:
        alert = {
            "level": "WARNING",
            "sensor": reading.sensor_type,
            "value": reading.value,
            "device": reading.device_id
        }
        ALERT_LOG.append(alert)
        alerts.append(alert)

    return alerts
