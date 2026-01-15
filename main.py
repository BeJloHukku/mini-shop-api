from fastapi import FastAPI

import uvicorn

from items_views import router as items_router
from users.views import router as users_router
from api_v1 import router as api_v1_router

from contextlib import asynccontextmanager
from core.config import settings
from core.models import Base, db_helper

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

app = FastAPI(lifespan=lifespan, title="Mini-shop")
app.include_router(items_router)
app.include_router(users_router)
app.include_router(api_v1_router, prefix=settings.api_v1_prefix )

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