from fastapi import APIRouter, Request, Depends, WebSocket
from fastapi.templating import Jinja2Templates
from typing import List

from app.attractions.router import get_attractions
from app.cities.router import get_cities, get_cities_by_id
from app.favoutites.router import get_favourites
from app.users.dependencies import get_current_user_id
from app.favoutites.router import get_cities_count

router = APIRouter(
    prefix="/pages",
    tags=["Frontend"]
)

templates = Jinja2Templates(directory="app/templates")

@router.get("/main")
async def get_main_page(
        request: Request,
        cities=Depends(get_cities)
):
    return templates.TemplateResponse(
        "mainPage.html",
        context={"request": request, "cities": cities})


@router.get("/register")
async def get_register_page(
        request: Request
):
    return templates.TemplateResponse("register.html", context={"request": request})


@router.get("/login")
async def get_login_page(
        request: Request
):
    return templates.TemplateResponse("login.html", context={"request": request})


@router.get("/{city_id}")
async def get_city_page(
        request: Request,
        city_id: int,
        city=Depends(get_cities_by_id)
):
    return templates.TemplateResponse(
        "city.html",
        context={"request": request, "city": city})


@router.get("/favourite/fav")
async def get_favourite(
        request: Request,
        user_id=Depends(get_current_user_id),
):
    favourites = await get_favourites(user_id)
    cities = []
    for i in range(len(favourites)):
        cities.append(await get_cities_by_id(favourites[i].city_id))
    return templates.TemplateResponse(
        "mainPage.html",
        context={"request": request, "cities": cities})
