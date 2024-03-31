from pydantic import BaseModel

# Validation


class SCities(BaseModel):
    id: int
    name: str
    location: str
    image_id: int
    description: str
    video_url: str

    class Config:
        orm_mode = True
