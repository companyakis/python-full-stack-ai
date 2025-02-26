from fastapi import FastAPI
from models.post import PersonPost

app = FastAPI()

person_posts = []

# post

@app.post("/post", response_model = PersonPost)
async def create_person_post(p: PersonPost):
    person_posts.append(p)
    return p

# get

@app.get("/posts", response_model = list[PersonPost])
async def get_person_posts():
    return person_posts
