from pydantic import BaseModel

# Validation


class SCities(BaseModel):
    id: int
    name: str
    longitude: str
    latitude: str
    image_id: int
    description: str
    video_url: str

    class Config:
        from_attributes = True
