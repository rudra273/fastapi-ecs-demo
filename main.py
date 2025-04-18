# main.py
from fastapi import FastAPI

# Create a FastAPI application instance
app = FastAPI()

# Define a simple API endpoint
@app.get("/")
async def read_root():
    """
    Root endpoint that returns a welcome message.
    """
    return {"message": "Hello, World! This is my first FastAPI on ECS (eventually)!"}

