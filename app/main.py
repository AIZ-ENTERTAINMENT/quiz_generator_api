"""
Main.py works as a main function for the application
Api app starts from here
"""

from contextlib import asynccontextmanager
from logging import getLogger
from logging.config import dictConfig
from os import environ

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.libs import sample_logger
from app.models import destroy_engine, setup_engine
from app.route.prompt import prompt_router
from app.route.quiz import quiz_router
from app.route.quiz_set import quiz_set_router
from app.route.topic import topic_router
from app.route.user import user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # When app starts
    await setup_engine()
    # await set_redis_configuration()
    yield
    await destroy_engine()
    # When app teardown


logger = getLogger(__name__)

app = FastAPI(
    docs_url=(
        "/quiz_generator/api/v1/docs"
        if environ.get("DEPLOY_PHASE", "dev") == "dev"
        or environ.get("DEPLOY_PHASE", "dev") == "local"
        else None
    ),
    lifespan=lifespan,
)

dictConfig(sample_logger)
app.include_router(user_router.router)
app.include_router(quiz_router.router)
app.include_router(topic_router.router)
app.include_router(prompt_router.router)
app.include_router(quiz_set_router.router)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # 실패한 요청에 대한 자세한 정보를 로그로 남깁니다.
    logger.error(f"Invalid request: {request.__dict__} - Errors: {exc.errors()}")
    # 클라이언트에게 구체적인 에러 메시지를 반환합니다.
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors(), "body": exc.body},
    )


origins = [
    "https://aiz-ailab.net",
    "http://aiz-ailab.net",
    "aiz-ailab.net",
    "https://mal2.aiz-ailab.net",
    "http://mal2.aiz-ailab.net",
    "http://dev.aiz-ailab.net",
    "https://dev.aiz-ailab.net",
    "dev.aiz-ailab.net",
]
if (
    environ.get("DEPLOY_PHASE", "dev") == "dev"
    or environ.get("DEPLOY_PHASE", "dev") == "local"
):
    origins.append("http://10.0.2.2:5173")  # app local url
    origins.append("http://localhost:5173")
    origins.append("http://localhost:4173")
    if environ.get("MOBILE_DEVICE_CORS_ADDRESS"):
        origins.append(environ.get("MOBILE_DEVICE_CORS_ADDRESS"))

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)