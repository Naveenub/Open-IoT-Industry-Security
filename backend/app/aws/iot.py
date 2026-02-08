import json

def parse_iot_message(payload: str):
    return json.loads(payload)
