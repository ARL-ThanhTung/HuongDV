from datetime import date
from pydantic import BaseModel , root_validator 
from typing import List
from app.schema.branch.branch import BranchResponse
from app.schema.category.category import CategoryResponse
from app.schema.product_detail.product_detail import ProductDetailResponse , ProductDetailBase
class ProductBase(BaseModel):
    title: str | None = None



class ProductRequest(ProductBase):
    title: str | None = None
    image: str | None = None
    description: str | None = None
    category_id: int | None = None
    branch_id: int | None = None
    #product_detail: List[ProductDetailBase] | None = None

class ProductRequestAll(ProductBase):
    title: str | None = None
    image: str | None = None
    description: str | None = None
    category_id: int | None = None
    branch_id: int | None = None
    product_detail: List[ProductDetailBase] | None = None

class ProductResponse(BaseModel):
    id: int | None = None
    title: str | None = None
    image: str | None = None
    description: str | None = None
    category: BranchResponse | None = None
    branch: CategoryResponse | None = None
    product_detail: List[ProductDetailResponse] | None = None
    class Config:
        orm_mode = True

class ProductUpdate(BaseModel):
    title: str | None = None
    image: str | None = None
    description: str | None = None
    category_id: int | None = None
    branch_id: int | None = None
    product_detail: List[ProductDetailBase] | None = None
    class Config:
        orm_mode = True




