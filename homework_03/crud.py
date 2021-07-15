from models import UserIn, User
from typing import Dict, Optional
from fastapi import Header, exceptions

USERS_BY_ID: Dict[int, User] = {}
USERS_BY_TOKEN: Dict[str, User] = {}


def create_user(user_in: UserIn):
    user = User(id=len(USERS_BY_ID) + 1, **user_in.dict())
    USERS_BY_ID[user.id] = user
    USERS_BY_TOKEN[user.token] = user
    return user


def get_user_by_id(user_id: int) -> Optional[User]:
    user = USERS_BY_ID.get(user_id)
    if user:
        return user

    raise exceptions.HTTPException(404, {"message": f"no user with id #{user_id}"})


def get_user_by_token(token: str = Header(..., description="User auth token")) -> Optional[User]:
    user = USERS_BY_TOKEN.get(token)
    if user:
        return user

    raise exceptions.HTTPException(404, {"message": "Invalid token"})
