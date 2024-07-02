from pydantic import BaseModel, Field


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str = Field(min_length=8)


class User(UserBase):
    id: int

    class Config:
        orm_mode = True