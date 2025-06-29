from fastapi import APIRouter, Body
from pydantic import EmailStr
from typing import Annotated

from .models import RegisterRequest, User

user_router = APIRouter(prefix='/user', tags=['user'])

# 1.vazifa
@user_router.post('/register')
async def register_user(user:RegisterRequest = Body(...)):
    return {'msg':f'{user.email} muvaffaqiyatli ro\'yxatdan o\'tdi'}

# 2.vazifa
@user_router.post('/comment')
async def post_comment(subject:str = Body() ,comment:str = Body(..., min_length=10, max_length=300)):
    return {'msg':f'{subject} mavzusidagi kommentingiz muvaffaqiyatli yuborildi'}

# 3.vazifa
@user_router.post('/update_profile')
async def update_prof(name:Annotated[str, Body(min_length=3)], age:Annotated[int, Body(ge=18, le=99)]):
    return {'msg':f'The name is set to {name}, and the age {age}'}

# 4.vazifa, 10.vazifa
@user_router.post('/create')
async def full_update(user:User = Body(...)):
    return {'msg':f'The {user.name} named user successfully created (email:{user.email} and age:{user.age})'}

# 8.vazifa
@user_router.post('/email_info')
async def recieve_email(email:Annotated[EmailStr, Body(...)]):
    return {'msg':f'your email is {email}'}