from fastapi import FastAPI
from pydantic.error_wrappers import ValidationError
from db import db
import configparser
import asyncio
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import redis
import pika

import neural_api.neural_api
import catalog_api.catalog_api

config = configparser.ConfigParser()
config.read("config.ini")
app_port = int(config["APP"]["port"])
app_host = config["APP"]["host"]
redis_port = int(config["REDIS"]["port"])
redis_host = config["REDIS"]["host"]
rabbit_port = int(config["RABBITMQ"]["port"])
rabbit_host = config["RABBITMQ"]["host"]
PSQL_DB = config["PSQL"]["PSQL_DB"]

app = FastAPI(host=app_host, port=app_port)

rabbit_connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=rabbit_host, port=rabbit_port)
)
channel_send = rabbit_connection.channel()
channel_send.queue_declare(queue="requests_queue")

redis_client = redis.Redis(host=redis_host, port=redis_port)

seen_basket = db.SeenBasket(redis_client)
compare_basket = db.CompareBasket(redis_client)
cart_basket = db.CartBasket(redis_client)

engine = create_engine(PSQL_DB)
Session = sessionmaker(bind=engine)
session = Session()

event_loop = asyncio.get_event_loop()


app.include_router(neural_api.neural_api.router,
                   prefix="/neural", tags=["neural"])
app.include_router(catalog_api.catalog_api.router,
                   prefix="/catalog", tags=["catalog"])
