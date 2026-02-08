import requests
from app.core.config import settings

def send_sms_alert(message: str):
    if not settings.SMS_ENABLED:
        return

    payload = {
        "To": settings.SMS_TO,
        "From": settings.SMS_FROM,
        "Body": message
    }

    try:
        requests.post(
            settings.SMS_API_URL,
            data=payload,
            auth=(settings.SMS_ACCOUNT_SID, settings.SMS_AUTH_TOKEN)
        )
    except Exception as e:
        print(f"[SMS ALERT ERROR] {e}")
