from fastapi import FastAPI
from app.api.routes import router
from app.core.config import settings

app = FastAPI(
    title="Open IoT Industry Security",
    description="Real-time Industrial IoT Security Monitoring API",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def root():
    return {"status": "running", "env": settings.ENV}
