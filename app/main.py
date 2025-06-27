from fastapi import FastAPI

from app import async_routes
from app.routes import router

app = FastAPI()
app.include_router(router)
app.include_router(async_routes.router, prefix="/testes")
