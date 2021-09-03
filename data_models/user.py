from pydantic import BaseModel


class UserFromNeuralApi(BaseModel):
    user_id: int
