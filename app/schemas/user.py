from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from typing import Optional


# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    name: Optional[str] = None
    created_at: Optional[datetime] = Field(default=None, description="Date and time the user was created")


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        from_attributes = True


# Additional properties to return via API
class User(UserInDBBase):
    pass


class PublicUser(BaseModel):
    name: Optional[str] = None


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
