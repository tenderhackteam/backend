from fastapi import FastAPI
from pydantic.error_wrappers import ValidationError
from db import db
import configparser

import redis

import neural_api.neural_api

config = configparser.ConfigParser()
config.read("config.ini")
app_port = int(config["APP"]["port"])
app_host = config["APP"]["host"]
redis_port = int(config["REDIS"]["port"])
redis_host = config["REDIS"]["host"]

app = FastAPI(host=app_host, port=app_port)

redis_client = redis.Redis(host=redis_host, port=redis_port)

seen_basket = db.SeenBasket(redis_client)
compare_basket = db.CompareBasket(redis_client)
cart_basket = db.CartBasket(redis_client)

app.include_router(neural_api.neural_api.router, prefix="/neural", tags=["neural"])
