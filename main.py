from fastapi import FastAPI

#my imports
from users import user_router, auth_router

app = FastAPI()
app.include_router(user_router)
app.include_router(auth_router)

@app.get('/')
async def greeter():
    return 'Hellou stranger'