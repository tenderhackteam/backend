from fastapi import APIRouter
from fastapi.exceptions import RequestValidationError
from fastapi.responses import Response
from data_models.user import UserFromNeuralApi
from data_models.item import ItemFromNeuralApi

import json

import app

router = APIRouter()

responses = {
    200: {"description": "Data were successfully stored.", "content": ""},
    400: {"description": "Something was wrong with the data.", "content": ""},
    500: {"description": "Neural api is not responding.", "content": ""},
}


@router.post("/seen", responses=responses)
async def add_to_seen_endpoint(user: UserFromNeuralApi, item: ItemFromNeuralApi):
    if (
        user.user_id in app.compare_basket
        and item.item_id in app.compare_basket[user.user_id]
    ):
        return
    if (
        user.user_id in app.seen_basket
        and item.item_id in app.seen_basket[user.user_id]
    ):
        app.seen_basket.delete(user.user_id, item.item_id)
        app.compare_basket.add(user.user_id, item.item_id)
        return
    app.seen_basket.add(user.user_id, item.item_id)


@router.post("/cart", responses=responses)
async def add_to_cart_endpoint(user: UserFromNeuralApi, item: ItemFromNeuralApi):
    app.cart_basket.add(user.user_id, item.item_id)


@router.post("/generate")
async def neural_generate(user: UserFromNeuralApi):
    return json.dumps(
        {
            "seen": app.seen_basket[user.user_id],
            "compare": app.compare_basket[user.user_id],
            "cart": app.cart_basket[user.user_id],
        }
    )


@router.post("/category")
async def neural_category_sort(user: UserFromNeuralApi):
    ...
