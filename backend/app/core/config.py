from pydantic import BaseSettings

class Settings(BaseSettings):
    ENV: str = "development"

    # Email
    EMAIL_ENABLED: bool = False
    EMAIL_FROM: str | None = None
    EMAIL_TO: str | None = None
    SMTP_HOST: str | None = None
    SMTP_PORT: int = 587
    SMTP_USER: str | None = None
    SMTP_PASS: str | None = None

    # SMS
    SMS_ENABLED: bool = False
    SMS_API_URL: str | None = None
    SMS_ACCOUNT_SID: str | None = None
    SMS_AUTH_TOKEN: str | None = None
    SMS_FROM: str | None = None
    SMS_TO: str | None = None

    # Webhook
    WEBHOOK_ENABLED: bool = False
    WEBHOOK_URL: str | None = None

    class Config:
        env_file = ".env"

settings = Settings()
