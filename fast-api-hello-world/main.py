from typing import Optional
from enum import Enum
from unittest.mock import Base
from pydantic import BaseModel
from pydantic import Field
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
        max_length=50
    )
    last_name: str = Field(
        ..., 
        min_length=1,
        max_length=50
    )
    age: int = Field(
        ...,
        gt=0,
        le=100
    )
    is_married: Optional[bool] = Field(default=None)
    hair_color: Optional[HairColor] = Field(default=None)

class Location(BaseModel):
    city: str
    state: str
    country: str

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
    