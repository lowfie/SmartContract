from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from app.database.models import Token


class CreateTokenIn(BaseModel):
    media_url: str
    owner: str


class CreteTokenOut(BaseModel):
    unique_hash: str
    tx_hash: str
    media_url: str
    owner: str


class TokenList(BaseModel):
    class TokenSchema(CreteTokenOut):
        id: int
    token_list: list[TokenSchema]


class TotalSupplySchema(BaseModel):
    totalSupply: int


Token_Pydantic = pydantic_model_creator(Token, name="Token")
