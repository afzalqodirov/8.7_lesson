from fastapi import FastAPI

#my imports
from users import user_router, auth_router
from versioning import v1_router, v2_router
from books import book_router

app = FastAPI()
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(v1_router)
app.include_router(v2_router)
app.include_router(book_router)

@app.get('/')
async def greeter():
    return 'Hellou stranger'