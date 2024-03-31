from fastapi import APIRouter

from app.cities.dao import CitiesDAO
from app.cities.scemas import SCities

router = APIRouter(
    prefix="/cities",
    tags=["Города"]
)


@router.get("")
async def get_cities() -> list[SCities]:
    return await CitiesDAO.find_all()

