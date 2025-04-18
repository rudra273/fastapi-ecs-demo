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

@app.get("/items/")
async def read_items():
    """
    Endpoint to return a list of items.
    """
    return {"items": ["item1", "item2", "item3"]}

# new line
