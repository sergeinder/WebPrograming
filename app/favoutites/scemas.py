from pydantic import BaseModel


# Validation


class SFavourites(BaseModel):
    id: int
    user_id: int
    attraction_id: int

    class Config:
        from_attributes = True
