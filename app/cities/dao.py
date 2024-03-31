from app.cities.models import Cities
from app.dao.base import BaseDAO


class CitiesDAO(BaseDAO):
    model = Cities
