from fastapi import FastAPI

# Contains the application
app = FastAPI()

# path operation
@app.get("/")
def home():
    return {"Hello": "World"}