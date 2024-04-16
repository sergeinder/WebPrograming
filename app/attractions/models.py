from sqlalchemy import Column, Integer, String

from app.src.database import Base


class Attractions(Base):
    __tablename__ = "attractions"

    id = Column(Integer, primary_key=True)
    city_id = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    longitude = Column(String, nullable=False)
    latitude = Column(String, nullable=False)
    address = Column(String, nullable=False)
    image_id = Column(Integer, nullable=False)

