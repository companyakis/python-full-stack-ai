from fastapi import FastAPI
from models.post import PersonPost

app = FastAPI()

person_posts = []

@app.post("/post")
async def create_person_post(p: PersonPost):
    person_posts.append(p)
    return p
