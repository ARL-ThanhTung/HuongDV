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
from app.model.base import Category
from app.schema.category.category import CategoryRequest , CategoryResponse , CategoryUpdate

# Get All 
@router.get(
    "" ,  response_model=List[CategoryResponse]
)
def get(  
    db: Session = Depends(get_db)
):
    try:
        res = db.query(Category).all()
        return res
    except Exception as exc:
        print(exc)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='BAD REQUEST')
    
# Get 
@router.get(
    "/{id}" ,  response_model=CategoryResponse, 
)
def get_by_id( id: int ,   
    db: Session = Depends(get_db)
):
    try:
        res = db.query(Category).filter( Category.id == id ).first()
        return res
    except Exception as exc:
        print(exc)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='BAD REQUEST')

@router.post(
    ""
)
def create( data: CategoryRequest , 
    db: Session = Depends(get_db)
):
    try:
        res = Category(**data.dict())
        db.add(res)
        db.commit()
        db.refresh(res)
        if res is not None:
            return HTTPException(status_code=status.HTTP_200_OK, detail='Success')
        else:
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='BAD REQUEST')
    except Exception as exc:
        print(exc)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='BAD REQUEST')
    
@router.put(
    "/{id}"
)
def update( id: int , data: CategoryUpdate , 
    db: Session = Depends(get_db)
):
    try:
        res = db.query(Category).filter( Category.id == id ).first()
        res.name = data.name

        db.add(res)
        db.commit()
        db.refresh(res)
        
        if res is not None:
            return HTTPException(status_code=status.HTTP_200_OK, detail='Success')
        else:
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='BAD REQUEST')
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
            res = db.query(Category).filter( Category.id == i ).first() 
            db.delete(res)
            db.commit()

        return HTTPException(status_code=status.HTTP_200_OK, detail='Success')
    except Exception as exc:
        print(exc)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='BAD REQUEST')


