import uvicorn
# from src.asgi import app

def run_server():
    uvicorn.run('src.asgi:app', reload=True, workers=8)