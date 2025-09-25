import logging
from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.core.config import get_settings
from app.core.database import engine
from app.models import base

logger = logging.getLogger(__name__)
settings = get_settings()


@asynccontextmanager
def lifespan(app: FastAPI):
    logger.info("Starting up Find Your Balance backend")
    async with engine.begin() as conn:
        await conn.run_sync(base.Base.metadata.create_all)
    yield
    logger.info("Shutting down Find Your Balance backend")


app = FastAPI(title=settings.app_name, lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.api_v1_prefix)


class ConnectionManager:
    def __init__(self) -> None:
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket) -> None:
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket) -> None:
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    async def broadcast(self, message: dict[str, Any]) -> None:
        for connection in self.active_connections:
            await connection.send_json(message)


manager = ConnectionManager()


@app.websocket("/ws/activity")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            payload = await websocket.receive_json()
            await manager.broadcast({"type": "activity", "payload": payload})
    except WebSocketDisconnect:
        manager.disconnect(websocket)


@app.get("/health")
async def healthcheck():
    return {"status": "ok"}
