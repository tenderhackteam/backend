from fastapi import APIRouter
from fastapi.exceptions import RequestValidationError
from fastapi.responses import Response
from data_models.user import UserFromNeuralApi
from data_models.item import ItemFromNeuralApi

router = APIRouter()

responses = {
    200: {"description": "Data were successfully stored.", "content": ""},
    400: {"description": "Something was wrong with the data.", "content": ""},
    500: {"description": "Neural api is not responding.", "content": ""},
}


@router.post("/seen", responses=responses)
async def add_to_seen_endpoint(user: UserFromNeuralApi, item: ItemFromNeuralApi):
    ...


@router.post("/cart", responses=responses)
async def add_to_cart_endpoint(user: UserFromNeuralApi, item: ItemFromNeuralApi):
    ...


@router.post("/generate", responses=responses)
async def neural_generate(user: UserFromNeuralApi):
    ...
