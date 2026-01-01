from fastapi import FastAPI, Path
from pydantic import BaseModel, EmailStr

import uvicorn

from items_views import router as items_router
from users.views import router as users_router

app = FastAPI(title="Mini-shop")
app.include_router(items_router)
app.include_router(users_router)

@app.get("/")
def hello_index():
    return {
        "message": "Hello index"
    }

@app.get("/hello/")
def hello(name: str = "World"):
    name = name.strip().title()
    return {
        "message": f"Hello {name}"
    }

@app.get("/calc/add/")
def add(a: int, b: int):
    return {
        "message": f"{a} + {b} = {a + b}"
    }



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)