from typing import Optional
from enum import Enum
from unittest.mock import Base
from pydantic import BaseModel, validator
from pydantic import Field, EmailStr, HttpUrl
from fastapi import FastAPI
from fastapi import Body, Query, Path

# Contains the application
app = FastAPI()

# Models

class HairColor(Enum):
    white = "white"
    brown = "brown"
    black = "black"
    blonde = "blonde"
    red = "red"
    
class Person(BaseModel):
    first_name: str = Field(
        ..., 
        min_length=1,
        max_length=50,
        example="Matilde"
    )
    last_name: str = Field(
        ..., 
        min_length=1,
        max_length=50,
        example="Fajardo"
    )
    age: int = Field(
        ...,
        gt=0,
        le=100,
        example=20,
    )
    password: str = Field(
        min_length=10, 
        max_length=20,
        example="123abcdefgg"
    )
    is_married: Optional[bool] = Field(default=None)
    hair_color: Optional[HairColor] = Field(default=None)
    email: Optional[EmailStr] = Field(
        default=None,
        example="nicolas@gmail.com"
    )
    web_page: Optional[HttpUrl] = Field(
        default=None,
        example="google.com"
    )
    
    # custom validation
    @validator('password')
    def passwords_match(cls, v):
        assert v.isalnum(), 'must be alphanumeric'
        return v

    # define default values to test the API in Swagger UI
    # must be named "example" for swagger to recognize it
    
    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "first_name": "Nicolás",
    #             "last_name": "Roldán",
    #             "age": 20,
    #             "password": "123abcdefgg",
    #             "hair_color": "blonde",
    #             "web_page": "google.com",
    #             "email": "nicolas@gmail.com"
    #         }
    #     }

class Location(BaseModel):
    city: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Bogotá"
    )
    state: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Cundinamarca"
    )
    country: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Colombia"
    )
    
    # Alternative way for defining default values for examples in
    # Swaggr UI.
    
    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "city": "Bogotá",
    #             "state": "Cundinamarca",
    #             "country": "Colombia",
    #         }
    #     }

# path operation
@app.get("/")
def home():
    return {"Hello": "World"}

@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person

# query params validations
@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(
        None, 
        min_length=1, 
        max_length=50,
        title="Person's Name",
        description="This is the person's name. Have to be between 1 and 50 characters."
    ),
    age: int = Query(
        ..., 
        ge=1, 
        lt=100, 
        title="Person's Age",
        description="This is the person's age. Have to be between 1 and 100 years. It's required."
    )
):
    return {name: age}

# path params validations
@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
        ..., 
        gt=0,
        title="Person's id.",
        description="This is the person's id. Have to be greater than 0. It's required."
    )
):
    return {person_id: "It exists."}

# request body validations
@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ..., 
        gt=0,
        title="Person's id.",
        description="This is the person's id. Have to be greater than 0. It's required."
    ),
    person: Person = Body(...),
    location: Location = Body(...)
):
    results = person.dict()
    results.update(location.dict())
    # easier way (not supported yet) person.dict() & location.dict()
    return results
    