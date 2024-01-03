from datetime import date
from pydantic import BaseModel , root_validator 
from typing import List
from app.schema.branch.branch import BranchResponse
from app.schema.category.category import CategoryResponse

class ProductDetailBase(BaseModel):
    ram: str | None = None
    rom: str | None = None
    os: str | None = None
    image: str | None = None
    description: str | None = None
    camera: str | None = None
    camera_self: str | None = None
    battery: int | None = None
    card: str | None = None
    video: str | None = None
    chip: str | None = None
    screen: str | None = None
    price: float | None = None
    quantity_remain: int | None = None

class ProductDetailRequest(ProductDetailBase):
    product_id: int | None = None


class ProductDetailResponse(BaseModel):
    id: int | None = None
    ram: str | None = None
    rom: str | None = None
    os: str | None = None
    image: str | None = None
    description: str | None = None
    camera: str | None = None
    camera_self: str | None = None
    battery: int | None = None
    card: str | None = None
    video: str | None = None
    chip: str | None = None
    screen: str | None = None
    price: float | None = None
    quantity_remain: int | None = None
    product_id: int | None = None
    
    class Config:
        orm_mode = True

class ProductDetailUpdate(BaseModel):
    ram: str | None = None
    rom: str | None = None
    os: str | None = None
    image: str | None = None
    description: str | None = None
    camera: str | None = None
    camera_self: str | None = None
    battery: int | None = None
    card: str | None = None
    video: str | None = None
    chip: str | None = None
    screen: str | None = None
    price: float | None = None
    quantity_remain: int | None = None
    product_id: int | None = None
    class Config:
        orm_mode = True


class ProductResponse(BaseModel):
    id: int | None = None
    title: str | None = None
    image: str | None = None
    description: str | None = None
    category: BranchResponse | None = None
    branch: CategoryResponse | None = None
    
    class Config:
        orm_mode = True


class ProductDetailResponseAll(BaseModel):
    id: int | None = None
    ram: str | None = None
    rom: str | None = None
    os: str | None = None
    image: str | None = None
    description: str | None = None
    camera: str | None = None
    camera_self: str | None = None
    battery: int | None = None
    card: str | None = None
    video: str | None = None
    chip: str | None = None
    screen: str | None = None
    price: float | None = None
    quantity_remain: int | None = None
    product: ProductResponse | None = None
    
    class Config:
        orm_mode = True

