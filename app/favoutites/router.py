from fastapi import APIRouter, Depends, Request


from app.favoutites.dao import FavouritesDAO
from app.users.models import Users
from app.users.dependencies import get_current_user

router = APIRouter(
    prefix="/favourites",
    tags=["Favourites"]
)


@router.get("")
async def get_favourites(user_id: int):
    return await FavouritesDAO.find_all(user_id = user_id)


@router.post("")
async def add_favourite(
        city_id: int,
        user: Users = Depends(get_current_user)
):
    favourites_of_user = await get_favourites(user.id)
    flag = True
    for favor in favourites_of_user:
        if favor.city_id == city_id:
            flag = False
            break
    if flag:
        await FavouritesDAO.add(user.id, city_id)
    




