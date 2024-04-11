from fastapi import FastAPI
from fastapi.responses import FileResponse
from task_2.models import User, UserAdult

app = FastAPI()

user = User(id=1, name="John Doe")

@app.get("/users", response_model=User)
async def get_user():
    return user

@app.post("/user", response_model=UserAdult)
async def get_user_1(user: UserAdult):
    user.is_adult = (user.age >= 18)
    return user
