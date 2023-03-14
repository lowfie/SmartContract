from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from app.web3.contract.ethereum_goerli import EthereumGoerliTestnet
from app.api.tokens.utils import generate_unique_hash
from app.database.models import Token
from app.settings.config import CONTRACT_ABI, CONTRACT_ADDRESS, METAMASK_PRIVATE_KEY
from app.api.tokens.schemas import (
    CreateTokenIn,
    CreteTokenOut,
    Token_Pydantic,
    TokenList,
    TotalSupplySchema
)


tokens = APIRouter()

contract = EthereumGoerliTestnet(
    contract_address=CONTRACT_ADDRESS,
    contract_abi=CONTRACT_ABI,
    private_key=METAMASK_PRIVATE_KEY
)


@tokens.post('/create/', response_model=CreteTokenOut)
async def create_new_token(create_token: CreateTokenIn):
    unique_hash = generate_unique_hash()
    try:
        tx_hash = contract.mint(
            owner_address=create_token.owner,
            unique_hash=unique_hash,
            mediaURL=create_token.media_url
        )
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
            detail="INSUFFICIENT_FUNDS"
        )
    token_result = CreteTokenOut(
        unique_hash=unique_hash,
        tx_hash=tx_hash,
        media_url=create_token.media_url,
        owner=create_token.owner
    )
    await Token.create(**token_result.dict(exclude_unset=True))
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"result": {"token": jsonable_encoder(token_result)}}
    )


@tokens.get('/list/', response_model=TokenList)
async def list_token_objects():
    token_list = await Token_Pydantic.from_queryset(Token.all())
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"token_list": jsonable_encoder(token_list)}
    )


@tokens.get('/total_supply/', response_model=TotalSupplySchema)
async def total_number_tokens():
    total_supply = contract.total_supply()
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"totalSupply": jsonable_encoder(total_supply)}
    )
