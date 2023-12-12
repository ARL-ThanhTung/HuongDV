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

from app.model.base import Product_Detail
from app.schema.product_detail.product_detail import (  ProductDetailRequest , 
                                                        ProductDetailResponse , 
                                                        ProductDetailResponseAll , 
                                                        ProductDetailUpdate , 
)
# Get All 
@router.get(
    "" ,  response_model=List[ProductDetailResponseAll]
)
def get(   product_id: int | None = None,
    db: Session = Depends(get_db)
):
    try:
        if product_id is not None:
            res = db.query(Product_Detail).filter(and_(Product_Detail.product_id == product_id )).all()
        else:
            res = db.query(Product_Detail).all()
        return res
    except Exception as exc:
        print(exc)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='BAD REQUEST')
    
# Get 
@router.get(
    "/{id}" ,  response_model=ProductDetailResponseAll, 
)
def get_by_id( id: int ,   
    db: Session = Depends(get_db)
):
    try:
        res = db.query(Product_Detail).filter( Product_Detail.id == id ).first()
        return res
    except Exception as exc:
        print(exc)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='BAD REQUEST')

@router.post(
    ""
)
def create( data: ProductDetailRequest , 
    db: Session = Depends(get_db)
):
    try:
        
        res = Product_Detail(**data.dict())
        db.add(res)
        db.commit()
        db.refresh(res)
        if res is None:
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='BAD REQUEST')
        
        return HTTPException(status_code=status.HTTP_200_OK, detail='Success')
    except Exception as exc:
        print(exc)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='BAD REQUEST')
    
@router.put(
    "/{id}"
)
def update( id: int , data: ProductDetailUpdate , 
    db: Session = Depends(get_db)
):
    try:
        res = db.query(Product_Detail).filter( Product_Detail.id == id ).first()
        if res is None:
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='BAD REQUEST')
        res.rom = data.title
        res.rom = data.rom
        res.os = data.os
        res.image = data.image
        res.description = data.description
        res.price = data.price
        res.camera = data.camera
        res.camera_self = data.camera_self
        res.battery = data.battery
        res.card = data.card
        res.video = data.video
        res.quantity_remain = data.quantity_remain
        res.chip = data.chip
        res.screen = data.screen
        res.product_id = data.product_id
        db.add(res)
        db.commit()
        db.refresh(res)
        if res is None:
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='BAD REQUEST')
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
            res = db.query(Product_Detail).filter( Product_Detail.id == i ).first() 
            db.delete(res)
            db.commit()
        return HTTPException(status_code=status.HTTP_200_OK, detail='Success')
    except Exception as exc:
        print(exc)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='BAD REQUEST')
