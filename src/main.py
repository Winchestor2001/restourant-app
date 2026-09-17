from fastapi import FastAPI

from src.api.v1 import main_router

app = FastAPI()

app.include_router(main_router)
