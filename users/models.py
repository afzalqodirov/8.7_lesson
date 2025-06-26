from pydantic import EmailStr, BaseModel, Field
from typing import Annotated

class RegisterRequest(BaseModel):
    email: EmailStr

# 6.vazifa
class User(BaseModel):
    name = Annotated[str, Field( description='the first name of users field', min_length=3, max_length=50, examples=['Afzal', 'Muhammadjon'])]
    email = Annotated[EmailStr, Field(..., description='the email field')]
    age = Annotated[int, Field(le=99, ge=18)]