from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import uuid
import uvicorn

app = FastAPI()

manager_connections = set()

def get_unique_id():
    return str(uuid.uuid4())

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print(f"Cliente: {websocket.client.host}")
    manager_connections.add(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"You said: {data}")
            for client in manager_connections:
                if client != websocket:
                    await client.send_text(f"Client says: {data}")
    except WebSocketDisconnect:
        manager_connections.remove(websocket)
    finally:
        await websocket.close()

@app.get("/")
async def get():
    return {"msg": "Hello World"}

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000)