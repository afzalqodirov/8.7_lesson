from fastapi import APIRouter, Body
from .models import Books

book_router = APIRouter(prefix='/books', tags=['book'])

# 9.vazifa
@book_router.post('/validator')
async def validationer(book:Books = Body(...)):
    return book