from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.models import destroy_engine, setup_engine
from app.route.user import user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # When app starts
    await setup_engine()
    # await set_redis_configuration()
    yield
    await destroy_engine()
    # When app teardown

app = FastAPI(
    docs_url="/quiz_generator/api/docs",
    lifespan=lifespan,
)

app.include_router(user_router.router)

@app.get("/")
def root():
    return {"message": "Quiz Generator SPHINX"}

@app.get("/home")
def home():
    return {"message": "Home"}