import requests
import random
import time

API = "http://localhost:8000/api/ingest"

SENSORS = ["temperature", "humidity", "smoke", "co", "flame"]

while True:
    payload = {
        "device_id": "factory-01",
        "sensor_type": random.choice(SENSORS),
        "value": random.randint(0, 100)
    }
    requests.post(API, json=payload)
    time.sleep(2)
