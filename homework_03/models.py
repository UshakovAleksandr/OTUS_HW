from datetime import datetime
from pydantic import BaseModel, Field
from uuid import uuid4


class UserIn(BaseModel):
    username: str


class UserBase(UserIn):
    id: int
    created_at: datetime = Field(default_factory=datetime.now)
    status: str = "active"


def generate_token():
    token = str(uuid4())
    print(token)
    return token


class User(UserBase):
    token: str = Field(default_factory=generate_token)


class UserOut(UserBase):
    pass
