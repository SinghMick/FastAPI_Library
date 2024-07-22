from typing import Optional
from pydantic import BaseModel

class Book(BaseModel):
    id: Optional[int] = None
    title: str
    author: str
    description: Optional[str] = None
