from fastapi import FastAPI

app = FastAPI()
   
@app.get("/")
def home():
    return {"message": "Hello, World!"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/greet")
def greet_person():
    return {"message": {"Hello person"}}