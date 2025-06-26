from fastapi import APIRouter

v1_router = APIRouter(prefix='/v1',tags=['routers'])
v2_router = APIRouter(prefix='/v2', tags=['routers'])

# 7.vazifa
@v1_router.get('/status')
async def get_status():
    return 'Version 1'

@v2_router.get('/status')
async def status_get():
    return 'Version 2'