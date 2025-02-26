from pydantic import BaseModel 

class PersonPost(BaseModel):
    title: str
    body: str
