from pydantic import BaseModel, EmailStr


class SUserAuth(BaseModel):
    email: EmailStr
    hash_password: str
