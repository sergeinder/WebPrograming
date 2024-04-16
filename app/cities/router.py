from fastapi import APIRouter
from aiocache import cached, SimpleMemoryCache

from app.cities.dao import CitiesDAO
from app.cities.scemas import SCities

router = APIRouter(
    prefix="/cities",
    tags=["Города"]
)

@router.get("")
async def get_cities() -> list[SCities]:
    return await CitiesDAO.find_all()


@router.get("")
async def get_cities_by_id(city_id: int) -> SCities:
    return await CitiesDAO.find_by_id(city_id)

