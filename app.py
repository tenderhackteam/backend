from fastapi import APIRouter, FastAPI
from pydantic.error_wrappers import ValidationError
from db import db

import neural_api.neural_api

app = FastAPI()

seen_basket = db.SeenBasket()
compare_basket = db.CompareBasket()
cart_basket = db.CartBasket()

app.include_router(neural_api.neural_api.router, prefix="/neural", tags=["neural"])
