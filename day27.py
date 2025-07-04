from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel, Field, field_validator,ValidationError
from fastapi import FastAPI,Depends
from typing import List

# Database Configuration
DATABASE_URL = "sqlite:///./test.db"  # Use SQLite for simplicity

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

#Table configuration
class Library(Base):
    __tablename__ = 'Library'
    
    book_id = Column(Integer,primary_key=True)
    book_name = Column(String(100))
    author_name = Column(String(100))
    publication_year = Column(Integer)

#Pydantic schema
class BookCreate(BaseModel):
    book_name:str = Field(description='Name of the book')
    author_name:str = Field(description='Name of the author of the book')
    publication_year:int = Field(description='Publication year of the book')
    
    @field_validator('publication_year')
    @classmethod
    def checking_publication_year(cls,year_value):
        if not (1000<=year_value<=9999):
            raise ValueError('Year must of 4 digit only')
        return year_value

class BookOut(BaseModel):
    book_id : int
    book_name:str
    author_name:str
    publication_year:int
    
    model_config = {
        "from_attributes": True
    }

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/book_info',response_model=List[BookOut])
async def get_books(db:Session=Depends(get_db)):
    books = db.query(Library).all()
    return books

@app.post('/book_info')
async def add_book(book:BookCreate,db:Session=Depends(get_db)):
    new_book = Library(book_name=book.book_name,
                    author_name = book.author_name,
                    publication_year = book.publication_year)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return {"message":"Book added successfully","book info":book}

@app.put('/book_info')
async def update_book(book_id:int,updated_book:BookCreate,db:Session=Depends(get_db)):
    book = db.query(Library).filter(Library.book_id==book_id).first()
    if not book:
        return {"message":"book not found kindly add it first"}
    
    book.book_name = updated_book.book_name
    book.author_name = updated_book.author_name
    book.publication_year = updated_book.publication_year
    
    db.commit()
    db.refresh(book)
    return {"message": "Book updated successfully", "book": updated_book}

@app.delete('/book_info')
async def delete_book(book_id:int,db:Session=Depends(get_db)):
    book = db.query(Library).filter(Library.book_id == book_id).first()
    if book is None:
        return {"message": "Book not found", "book_id": book_id}
    db.delete(book)
    db.commit()
    return {"message": "Book deleted successfully", "book_id": book_id}
