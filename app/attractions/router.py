from fastapi import APIRouter

from app.attractions.dao import AttractionsDAO
from app.attractions.scemas import SAttractions

router = APIRouter(
    prefix="/attractions",
    tags=["Attractions"]
)


@router.get("")
async def get_attractions(city_id: int) -> list[SAttractions]:
    return await AttractionsDAO.find_all(id=city_id)

