import requests
from app.core.config import settings

def send_webhook_alert(payload: dict):
    if not settings.WEBHOOK_ENABLED:
        return

    try:
        requests.post(settings.WEBHOOK_URL, json=payload, timeout=3)
    except Exception as e:
        print(f"[WEBHOOK ALERT ERROR] {e}")
