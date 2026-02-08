from pydantic import BaseSettings

class Settings(BaseSettings):
    ENV: str = "development"
    ALERT_EMAIL: str | None = None

    class Config:
        env_file = ".env"

settings = Settings()
