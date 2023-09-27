import http
from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse
from src.core.routers.api.v1.routers import router as api_v1_router


def app_description():
    _app = FastAPI(title="Project Lumina", version="1.0", docs_url="/api/v1/docs", redirect_slashes=False)

    return _app


app = app_description()
app.middleware('http')


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