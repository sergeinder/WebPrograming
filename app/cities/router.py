from typing import List

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.cities.dao import CitiesDAO
from app.cities.scemas import SCities
from app.favoutites.router import get_cities_count

router = APIRouter(
    prefix="/cities",
    tags=["Города"]
)


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


@router.get("")
async def get_cities() -> list[SCities]:
    return await CitiesDAO.find_all()


@router.get("")
async def get_cities_by_id(city_id: int) -> SCities:
    return await CitiesDAO.find_by_id(city_id)

@router.post("")
async def add_city(
    id : int,
    name: str,
    longitude: str,
    latitude: str, 
    image_id: int,
    big_photo_id: int, 
    description:str 
):
    return await CitiesDAO.add(id=id, name=name, longitude=longitude,latitude=latitude, image_id=image_id, big_photo_id=big_photo_id,description=description)


@router.websocket("/ws/{city_id}")
async def websocket_endpoint(websocket: WebSocket, city_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            truly_data = await get_cities_count(city_id)
            await manager.broadcast(f"{truly_data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
