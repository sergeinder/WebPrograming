from app.cities.models import Cities
from app.dao.base import BaseDAO
from app.src.database import asinc_session_maker

from sqlalchemy import insert

class CitiesDAO(BaseDAO):
    model = Cities
    @classmethod
    async def add(
            cls,
            id : int,
            name: str,
            longitude: str,
            latitude: str, 
            image_id: int,
            big_photo_id: int, 
            description:str 
    ):
        async with asinc_session_maker() as session:
            add_cities = insert(Cities).values(
                id=id,
                name=name,
                longitude=longitude,
                latitude=latitude,
                image_id=image_id,
                big_photo_id=big_photo_id,
                description=description
            )
            new_cities = await session.execute(add_cities)
            await session.commit()
            return new_cities.scalar()
