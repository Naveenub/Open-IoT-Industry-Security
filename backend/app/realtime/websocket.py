from fastapi import WebSocket

active_clients = []

async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    active_clients.append(ws)

    try:
        while True:
            await ws.receive_text()
    except:
        active_clients.remove(ws)

async def broadcast(data: dict):
    for ws in active_clients:
        await ws.send_json(data)
