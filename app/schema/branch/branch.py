from datetime import date
from pydantic import BaseModel , root_validator 
from typing import List


class BranchBase(BaseModel):
    name: str | None = None
    image: str | None = None 

class BranchRequest(BranchBase):
    name: str | None = None
    image: str | None = None 

class BranchResponse(BaseModel):
    id: int | None = None
    name: str | None = None
    image: str | None = None 

    class Config:
        orm_mode = True

class BranchUpdate(BaseModel):
    name: str | None = None
    image: str | None = None 
    class Config:
        orm_mode = True

