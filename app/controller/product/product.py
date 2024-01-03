from fastapi import APIRouter, Depends, HTTPException, status, Request
import logging
from fastapi_sqlalchemy import db
from sqlalchemy import and_
logger = logging.getLogger()
from typing import List
from sqlalchemy.orm import Session
from app.db.base import get_db
from datetime import datetime
router = APIRouter()
from fastapi.encoders import jsonable_encoder
from datetime import date
from sqlalchemy import and_
from app.model.base import Product
from app.model.base import Product_Detail
from app.schema.product.product import ProductRequest , ProductRequestAll , ProductResponse , ProductUpdate
from app.schema.product_detail.product_detail import ProductDetailRequest
from app.services.product_detail.product_detail import ProductDetailService

# Get All 
@router.get(
    "" ,  response_model=List[ProductResponse]
)
def get(   category_id: int | None = None, branch_id: int | None = None, 
    db: Session = Depends(get_db)
):
    try:
        if category_id is not None and branch_id is not None:
            res = db.query(Product).filter(and_(Product.category_id == category_id , Product.branch_id==branch_id)).all()
        elif branch_id is not None:
            res = db.query(Product).filter(and_( Product.branch_id==branch_id)).all()
        elif category_id is not None:
            res = db.query(Product).filter(and_( Product.category_id == category_id )).all()
        else:
            res = db.query(Product).all()
        return res
    except Exception as exc:
        print(exc)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='BAD REQUEST')
    
# Get 
@router.get(
    "/{id}" ,  response_model=ProductResponse, 
)
def get_by_id( id: int ,   
    db: Session = Depends(get_db)
):
    try:
        res = db.query(Product).filter( Product.id == id ).first()
        if res is None:
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='BAD REQUEST')
        return res
    except Exception as exc:
        print(exc)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='BAD REQUEST')

@router.post(
    ""
)
def create( data: ProductRequestAll , 
    db: Session = Depends(get_db)
):
    try:
        req = ProductRequest(**data.dict())
        res = Product(**req.dict())
        db.add(res)
        db.commit()
        db.refresh(res)
        if res is None:
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='BAD REQUEST')
        product_id = res.id
        if len(data.product_detail) > 0:
            for i in data.product_detail:
                pd = ProductDetailRequest(**i.dict())
                pd.product_id = product_id
                product_detail = ProductDetailService.createProductDetail( pd , db=db )
        return HTTPException(status_code=status.HTTP_200_OK, detail='Success')
    except Exception as exc:
        print(exc)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='BAD REQUEST')
    
@router.put(
    "/{id}"
)
def update( id: int , data: ProductUpdate , 
    db: Session = Depends(get_db)
):
    try:
        res = db.query(Product).filter( Product.id == id ).first()
        if res is None:
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='BAD REQUEST')
        res.title = data.title
        res.image = data.image
        res.description = data.description
        res.category_id = data.category_id
        res.branch_id = data.branch_id
        db.add(res)
        db.commit()
        db.refresh(res)
        if res is None:
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='BAD REQUEST')
        product_id = res.id
        product_detail = db.query(Product_Detail).filter( and_( Product_Detail.product_id == product_id )).all()
        for i in product_detail:
            db.delete(i)
            db.commit()
        if len(data.product_detail) > 0:
            for i in data.product_detail:
                pd = ProductDetailRequest(**i.dict())
                pd.product_id = product_id
                product_detail = ProductDetailService.createProductDetail( pd , db=db )
        return HTTPException(status_code=status.HTTP_200_OK, detail='Success')
    except Exception as exc:
        print(exc)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='BAD REQUEST')
    
@router.delete(
    "" , 
)
def delete( id: List[int] , 
    db: Session = Depends(get_db)
):
    try:
        for i in id: 
            product_detail = db.query(Product_Detail).filter( and_( Product_Detail.product_id == i )).all()
            for j in product_detail:
                db.delete(j)
                db.commit()
            res = db.query(Product).filter( Product.id == i ).first() 
            db.delete(res)
            db.commit()
            
        return HTTPException(status_code=status.HTTP_200_OK, detail='Success')
    except Exception as exc:
        print(exc)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='BAD REQUEST')


# {
#   "title": "Laptop Dell Inpison",
#   "image": "image.png",
#   "description": "Đẹp xịn",
#   "category_id": 1,
#   "branch_id": 2,
#   "product_detail": [
#     {
#       "ram": "8",
#       "rom": "256",
#       "os": "Window 11",
#       "image": "image.png",
#       "description": "Mạnh",
#       "camera": "8",
#       "camera_self": "8",
#       "battery": "4",
#       "card": "NVIDIA 1650",
#       "video": "image",
#       "chip": "I5 12500H",
#       "screen": "15.6",
#       "price": 20900000,
#       "quantity_remain": 40
#     } , 
#     {
#       "ram": "8",
#       "rom": "512",
#       "os": "Window 11",
#       "image": "image.png",
#       "description": "Mạnh , bộ nhớ lớn",
#       "camera": "8",
#       "camera_self": "8",
#       "battery": "4",
#       "card": "NVIDIA 1650",
#       "video": "image",
#       "chip": "I5 13700H",
#       "screen": "15.6",
#       "price": 24900000,
#       "quantity_remain": 55
#     }
#   ]
# }