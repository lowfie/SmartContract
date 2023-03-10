from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

healthcheck = APIRouter()


@healthcheck.get('/healthcheck/', summary='healthcheck')
async def healthcheck_get_method():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={'result': 'response is work'}
    )
