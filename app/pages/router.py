from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from app.cities.router import get_cities

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


@router.get("/city/{city_name}")
async def get_city_page(
        city_name: str,
        request: Request,
        cities=Depends(get_cities)
):
    return templates.TemplateResponse(
        "city.html",
        context={"request": request, "cities": cities, "city_name": city_name})

