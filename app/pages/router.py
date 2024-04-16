from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from app.attractions.router import get_attractions
from app.cities.router import get_cities, get_cities_by_id
from app.favoutites.router import get_favourites
from app.users.dependencies import get_current_user

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
        attractions=Depends(get_attractions),
        city=Depends(get_cities_by_id)
):
    return templates.TemplateResponse(
        "city.html",
        context={"request": request, "attractions": attractions, "city": city})


@router.get("/favourite/{user_id}")
async def get_favourite(
        request: Request,
        user_id: int,
        favoutites=Depends(get_favourites)
):
    cities = []
    for i in range(len(favoutites)):
        cities.append(await get_cities_by_id(favoutites[i].city_id))
    return templates.TemplateResponse(
        "mainPage.html",
        context={"request": request, "cities": cities})