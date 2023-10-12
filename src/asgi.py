import http
from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse
from src.database.lifespan import on_shutdown, start_db
from src.core.routers.api.v1.routers import router as api_v1_router
from src.config.settings import config
from fastapi.middleware.cors import CORSMiddleware


def app_description():
    _app = FastAPI(
        title="Project Lumina",
        version="1.0",
        docs_url="/api/v1/docs",
        redirect_slashes=False,
    )

    origins = ["*"]
    if config.backend_cors_origin:
        origins = config.backend_cors_origin.split(",")

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


app = app_description()
app.middleware("http")


@app.on_event("startup")
async def start_broker():
    await start_db(app)


@app.on_event("shutdown")
async def end_broker():
    await on_shutdown()


@app.get("/")
async def say_hello():
    return {"message": "Base URL for School Management System"}


@app.get("/docs")
async def get_docs():
    return RedirectResponse(
        url=app.docs_url, status_code=status.HTTP_301_MOVED_PERMANENTLY
    )


@app.get("/redoc")
async def get_docs():
    return RedirectResponse(
        url=app.docs_url, status_code=status.HTTP_301_MOVED_PERMANENTLY
    )


app.include_router(prefix="/api/v1", router=api_v1_router)
