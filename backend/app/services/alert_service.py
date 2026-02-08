from app.core.thresholds import THRESHOLDS
from app.models.sensor import SensorReading
from app.services.notifier.email import send_email_alert
from app.services.notifier.sms import send_sms_alert
from app.services.notifier.webhook import send_webhook_alert

ALERT_LOG = []

def check_alerts(reading: SensorReading | None, fetch_all: bool = False):
    if fetch_all:
        return ALERT_LOG

    rules = THRESHOLDS.get(reading.sensor_type)
    if not rules:
        return []

    alert = None

    if "critical" in rules and reading.value >= rules["critical"]:
        alert = build_alert("CRITICAL", reading)

    elif "warning" in rules and reading.value >= rules["warning"]:
        alert = build_alert("WARNING", reading)

    if alert:
        ALERT_LOG.append(alert)
        notify(alert)
        return [alert]

    return []

def build_alert(level, reading):
    return {
        "level": level,
        "sensor": reading.sensor_type,
        "value": reading.value,
        "device": reading.device_id
    }

def notify(alert):
    message = f"[{alert['level']}] {alert['sensor']} = {alert['value']} on {alert['device']}"

    send_email_alert("IoT Security Alert", message)
    send_sms_alert(message)
    send_webhook_alert(alert)
