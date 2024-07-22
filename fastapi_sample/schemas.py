from typing import List
from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author: str
    description: str

class BookUpdate(BaseModel):
    title: str
    author: str
    description: str

class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    description: str

    class Config:
        orm_mode = True
