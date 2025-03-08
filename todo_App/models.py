from pydantic import BaseModel, Field
from typing import Optional

class TodoCreate(BaseModel):
    title:str
    description:Optional[str]=None

class TodoUpdate(BaseModel):
    title:Optional[str]
    description:Optional[str]

class TodoResponse(BaseModel):
    id:str=Field(alias="_id")
    title:str
    description:Optional[str]