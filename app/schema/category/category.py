from datetime import date
from pydantic import BaseModel , root_validator 
from typing import List


class CategoryBase(BaseModel):
    name: str | None = None

class CategoryRequest(CategoryBase):
    name: str | None = None

class CategoryResponse(BaseModel):
    id: int | None = None
    name: str | None = None
    class Config:
        orm_mode = True

class CategoryUpdate(BaseModel):
    name: str | None = None
    class Config:
        orm_mode = True

