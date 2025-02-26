from fastapi import FastAPI
from models.post import PersonPost

app = FastAPI()

@app.post("/post")
async def create_person_post(p: PersonPost):
    return p
