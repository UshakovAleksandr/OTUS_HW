from fastapi import FastAPI, Depends
from models import User, UserOut
import crud

app = FastAPI()


@app.get("/ping")
def get_status():
    return {"message": "pong"}


@app.post("/users", response_model=UserOut, tags=["Users"])
def create_user(user: User = Depends(crud.create_user)):
    return user


@app.get("/users/me", response_model=UserOut, tags=["Users"])
def get_me(user: User = Depends(crud.get_user_by_token)):
    return user


@app.get("/users/{user_id}", response_model=UserOut, tags=["Users"])
def get_user_by_id(user: User = Depends(crud.get_user_by_id)):
    return user
