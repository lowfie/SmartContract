from fastapi import APIRouter

tokens = APIRouter()


@tokens.post('/create/')
async def create_new_token():
    pass


@tokens.get('/list/')
async def list_token_objects():
    pass


@tokens.get('/total_supply/')
async def total_number_tokens():
    pass
