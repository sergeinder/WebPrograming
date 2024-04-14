from fastapi import APIRouter, Depends


from app.favoutites.dao import FavouritesDAO
from app.users.models import Users
from app.users.dependencies import get_current_user

router = APIRouter(
    prefix="/favourites",
    tags=["Favourites"]
)


@router.get("")
async def get_favourites(user: Users = Depends(get_current_user)):  # -> list[SFavourites]:
    return await FavouritesDAO.find_all(user_id=user.id)


@router.post("")
async def add_favourite(
        city_id: int,
        user: Users = Depends(get_current_user)
):
    favourites = await FavouritesDAO.add(user.id, city_id)
    if not favourites:
        print("fun, mfk")
