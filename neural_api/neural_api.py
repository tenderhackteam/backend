from fastapi import APIRouter, WebSocket
from fastapi.exceptions import RequestValidationError
from fastapi.responses import Response
from data_models.user import UserFromNeuralApi
from data_models.item import ItemFromNeuralApi
from neural_api.rpc_client import NeuralRpcClient

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
    if app.compare_basket.is_member(user.user_id, item.item_id):
        return
    if not app.seen_basket.add(user.user_id, item.item_id):
        app.seen_basket.delete(user.user_id, item.item_id)
        app.compare_basket.add(user.user_id, item.item_id)


@router.post("/cart", responses=responses)
async def add_to_cart_endpoint(user: UserFromNeuralApi, item: ItemFromNeuralApi):
    app.cart_basket.add(user.user_id, item.item_id)


@router.post("/generate")
async def neural_generate(user: UserFromNeuralApi, top_n: int):
    neural_rpc = await NeuralRpcClient(app.event_loop).connect()
    response = await neural_rpc.call(
        json.dumps(
            {
                "item_id": app.seen_basket[user.user_id] + app.compare_basket[user.user_id] + app.cart_basket[user.user_id],
                "top_n": top_n,
            }
        )
    )
    return response


@router.post("/category")
async def neural_category_sort(user: UserFromNeuralApi):
    ...
