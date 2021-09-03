from pydantic import BaseModel


class ItemFromNeuralApi(BaseModel):
    item_id: int
