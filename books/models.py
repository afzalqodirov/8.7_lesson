from pydantic import BaseModel, Field
from typing import Annotated

class Books(BaseModel):
    title:Annotated[str, Field(...)]
    author:Annotated[str, Field(...)] = "Noma'lum default qiymat"
    pages:Annotated[int, Field(gt=0)]