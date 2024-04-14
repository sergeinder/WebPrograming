from app.attractions.models import Attractions
from app.dao.base import BaseDAO


class AttractionsDAO(BaseDAO):
    model = Attractions
