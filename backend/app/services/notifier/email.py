import smtplib
from email.mime.text import MIMEText
from app.core.config import settings

def send_email_alert(subject: str, message: str):
    if not settings.EMAIL_ENABLED:
        return

    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = settings.EMAIL_FROM
    msg["To"] = settings.EMAIL_TO

    try:
        with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
            server.starttls()
            server.login(settings.SMTP_USER, settings.SMTP_PASS)
            server.send_message(msg)
    except Exception as e:
        print(f"[EMAIL ALERT ERROR] {e}")
