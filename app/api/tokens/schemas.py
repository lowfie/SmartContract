from pydantic import BaseModel


class CreateTokenIn(BaseModel):
    media_url: str
    owner: str


class CreteTokenOut(BaseModel):
    unique_hash: str
    tx_hash: str
    media_url: str
    owner: str
