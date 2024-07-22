from fastapi import FastAPI, HTTPException, Path, Query
from typing import List
from fastapi_sample.models import Book
from fastapi_sample.schemas import BookCreate, BookUpdate, BookResponse
from fastapi_sample.database import book_db

app = FastAPI()

@app.post("/books/", response_model=BookResponse)
def create_book(book: BookCreate):
    new_book = Book(id=len(book_db) + 1, **book.dict())
    book_db.append(new_book)
    return new_book

@app.get("/books/", response_model=List[BookResponse])
def get_books(skip: int = 0, limit: int = 10):
    return book_db[skip: skip + limit]

@app.get("/books/{book_id}", response_model=BookResponse)
def get_book(book_id: int = Path(..., description="The ID of the book to retrieve")):
    for book in book_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.put("/books/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book: BookUpdate):
    for index, existing_book in enumerate(book_db):
        if existing_book.id == book_id:
            updated_book = Book(id=book_id, **book.dict())
            book_db[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}", response_model=BookResponse)
def delete_book(book_id: int):
    for index, book in enumerate(book_db):
        if book.id == book_id:
            removed_book = book_db.pop(index)
            return removed_book
    raise HTTPException(status_code=404, detail="Book not found")
