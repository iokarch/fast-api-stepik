from fastapi import FastAPI
from fastapi.responses import FileResponse
from task_3.models import User, UserAdult, Feedback

app = FastAPI()

user = User(id=1, name="John Doe")

list_of_feedback = []


@app.post("/feedback")
async def get_user_1(feedback: Feedback):
    list_of_feedback.append(feedback)
    return {"message": f"Feedback received. Thank you, {feedback.name}!"}