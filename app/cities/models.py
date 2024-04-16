from sqlalchemy import Column, Integer, String

from app.src.database import Base


class Cities(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    longitude = Column(String, nullable=False)
    latitude = Column(String, nullable=False)
    image_id = Column(Integer)
    big_photo_id = Column(Integer)
    description = Column(String, nullable=False)