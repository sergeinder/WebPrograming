from sqlalchemy import Column, Integer

from app.src.database import Base


class Favourites(Base):
    __tablename__ = "favourites"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    city_id = Column(Integer, nullable=False)

