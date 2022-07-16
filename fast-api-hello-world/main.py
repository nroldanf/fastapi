from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi import Body, Query, Path

# Contains the application
app = FastAPI()

# Models
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None

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