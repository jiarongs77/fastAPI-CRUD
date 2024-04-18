from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


# Shared properties
class UserBase(BaseModel):
    email: EmailStr | None = None
    is_active: bool | None = True
    is_superuser: bool = False
    name: str | None = None
    created_at: datetime | None = Field(
        default=None, description="Date and time the user was created"
    )


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: str | None = None


class UserInDBBase(UserBase):
    id: int | None = None

    class Config:
        from_attributes = True


# Additional properties to return via API
class User(UserInDBBase):
    pass


class PublicUser(BaseModel):
    name: str | None = None


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
