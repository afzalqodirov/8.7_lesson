from fastapi import APIRouter

auth_router = APIRouter(prefix='users')

# 5.vazifa
@auth_router.post('login')
async def login():
    return 'Successfully logged in'

@auth_router.post('logout')
async def logout():
    return 'Successfully logged out'
# end 5.vazifa