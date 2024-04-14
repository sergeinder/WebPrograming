from sqlalchemy import insert

from app.favoutites.models import Favourites
from app.dao.base import BaseDAO
from app.src.database import asinc_session_maker


class FavouritesDAO(BaseDAO):
    model = Favourites

    @classmethod
    async def add(
            cls,
            user_id: int,
            city_id: int
    ):
        async with asinc_session_maker() as session:
            add_favourite = insert(Favourites).values(
                user_id=user_id,
                city_id=city_id
            )
            new_favourites = await session.execute(add_favourite)
            await session.commit()
            return new_favourites.scalar()
