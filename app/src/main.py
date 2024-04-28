from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import requests

from app.pages.router import router as router_pages
from app.cities.router import router as router_cities
from app.users.router import router as router_users
from app.favoutites.router import router as router_favourites
from app.attractions.router import router as router_attractions

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), "static")


app.include_router(router_users)
app.include_router(router_pages)
app.include_router(router_cities)
app.include_router(router_favourites)
app.include_router(router_attractions)


# Рудимент, забей
@app.get('/get_first_user')
def first_user():
    api_url = "https://jsonplaceholder.typicode.com/users"
    all_users = requests.get(api_url).json()
    user1 = all_users[0]
    name = user1["name"]
    email = user1["email"]
    return {'name': name, "email": email}
