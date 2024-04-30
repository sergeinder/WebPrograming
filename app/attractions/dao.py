from app.attractions.models import Attractions
from app.dao.base import BaseDAO

from app.src.database import asinc_session_maker

from sqlalchemy import insert

class AttractionsDAO(BaseDAO):
    model = Attractions
    @classmethod
    async def add(
            cls,
            id : int,
            city_id: int,
            name: str,
            description:str,
            longitude: str,
            latitude: str,
            address:str, 
            image_id: int, 
    ):
        async with asinc_session_maker() as session:
            add_attraction = insert(Attractions).values(
                id=id,
                city_id=city_id,
                name=name,
                description=description,
                longitude=longitude,
                latitude=latitude,
                address=address,
                image_id=image_id,
            )
            new_attractions = await session.execute(add_attraction)
            await session.commit()
            return new_attractions.scalar()
