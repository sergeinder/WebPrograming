from pydantic import BaseModel

# Validation


class SAttractions(BaseModel):
    id: int
    city_id: int
    name: str
    description: str
    longitude: str
    latitude: str
    address: str
    image_id: int

    class Config:
        from_attributes = True
