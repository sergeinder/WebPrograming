from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.pages.router import router as router_pages

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), "static")

app.include_router(router_pages)
