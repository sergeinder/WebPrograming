from fastapi import APIRouter, Depends

from app.attractions.dao import AttractionsDAO
from app.attractions.scemas import SAttractions
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/attractions",
    tags=["Attractions"]
)


@router.get("")
async def get_attractions(city_id: int) -> list[SAttractions]:
    return await AttractionsDAO.find_all(city_id=city_id)

@router.post("")
async def add_attractions(
    id : int,
    city_id: int,
    name: str,
    description:str,
    longitude: str,
    latitude: str,
    address:str, 
    image_id: int, 
):
    return await AttractionsDAO.add(id=id, city_id=city_id, name=name, description=description, longitude=longitude, latitude=latitude, address=address, image_id=image_id)
    