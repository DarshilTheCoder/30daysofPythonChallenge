#Today I am Learning about FastAPI. Get method is used to read the data, Post method is used to create new data like create new order, Put method is used to update the data, and Delete is used to delete the data. This four are most popular endpoints. 
#FastAPI offers in-built data validation. Here today, i build CRUD application where, user can creat a book using a FastAPI Swagger UI by post method, that get stored into library which is a list of dictonaries, then read the book from that library using GET method, update the book using put method and can delete the book using delete method. Moreover, nowadays I am fall in love with pydantic model to init the object or creating a class rather than traditional method of using __init__ method, as it provides a lot of other functionality. 

from pydantic import (BaseModel,Field,field_validator,ValidationError)
from fastapi import FastAPI
from enum import Enum
import string,random


app = FastAPI() #instance of an fastapi

def book_id_generator():
    id ="".join(random.choices(string.digits,k=5))
    return int(id)

library = [{'book_id':12345,
            'book_name':'avenger',
            'author_name':'marvel',
            'publication_year':2002}, 
            {'book_id':54321,
            'book_name':'captain_america',
            'author_name':'marvel',
            'publication_year':2004}]

class book_info(BaseModel):
    book_id:int = Field(default_factory=book_id_generator,description='id of the book',init=False)
    book_name:str = Field(description='name of the book')
    author_name:str = Field(description='name of the author')
    publication_year:int = Field(description='publication year of the book')
    
    @field_validator('publication_year')
    @classmethod
    def publication_year_validator(cls,year_value):
        if not (1000<=year_value<=9999):
            raise ValueError('year should be of 4 digits')
        return year_value
    
class BookCreate(BaseModel):
    book_name:str = Field(description='name of the book')
    author_name:str = Field(description='name of the author')
    publication_year:int = Field(description='publication year of the book')
    
    @field_validator('publication_year')
    @classmethod
    def publication_year_validator(cls,year_value):
        if not (1000<=year_value<=9999):
            raise ValueError('year should be of 4 digits')
        return year_value

@app.get('/book_info')
async def get_book():
    return library

@app.post('/book_info')
async def add_book(new_book:BookCreate):
    new_book_dict = book_info(**new_book.model_dump())#converts pydantic model into dict
    library.append(new_book_dict.model_dump())
    return {'message':'book added successfully','new_book':new_book}

@app.put('/update_book_info')
async def update_book_info(book_id:int,updated_book:BookCreate):
    for index,book in enumerate(library):
        if book['book_id']==book_id:
            updated_book_dict = updated_book.model_dump()
            library[index]= {'book_id':book_id,
                            'book_name':updated_book_dict['book_name'],
                            'author_name':updated_book_dict['author_name'],
                            'publication_year':updated_book_dict['publication_year']}
            return {"message": "Book updated","book_id":book_id, "book": updated_book_dict}
    return {f"Sorry book is not found. Kindly add it first"}

@app.delete('/delete_book')
async def delete_book(book_id:int):
    for book in library:
        if book['book_id']==book_id:
            library.remove(book)
            return {"message":"book deleted successfully","book_id":book_id}
    return {f"Sorry book is not found. Kindly add it first"}
