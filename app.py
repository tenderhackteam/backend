from fastapi import APIRouter, FastAPI
from pydantic.error_wrappers import ValidationError

from neural_api import neural_api

app = FastAPI()

app.include_router(neural_api.router, prefix="/neural", tags=["neural"])
