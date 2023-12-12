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

from app.schema.branch.branch import BranchRequest , BranchResponse , BranchUpdate 
from app.model.base import Branch

# Get All 
@router.get(
    "" ,  response_model=List[BranchResponse]
)
def get(  
    db: Session = Depends(get_db)
):
    try:
        branch = db.query(Branch).all()
        return branch
    except Exception as exc:
        print(exc)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='BAD REQUEST')
    
# Get All   Request  get_filter
@router.get(
    "/{id}" ,  response_model=BranchResponse, 
)
def get_by_id( id: int ,   
    db: Session = Depends(get_db)
):
    try:
        branch = db.query(Branch).filter( Branch.id == id ).first()
        return branch
    except Exception as exc:
        print(exc)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='BAD REQUEST')

@router.post(
    ""
)
def create( data: BranchRequest , 
    db: Session = Depends(get_db)
):
    try:
        branch = Branch(**data.dict())
        db.add(branch)
        db.commit()
        db.refresh(branch)
        if branch is not None:
            return HTTPException(status_code=status.HTTP_200_OK, detail='Success')
        else:
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='BAD REQUEST')
    except Exception as exc:
        print(exc)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='BAD REQUEST')
    
@router.put(
    "/{id}"
)
def update( id: int , data: BranchUpdate , 
    db: Session = Depends(get_db)
):
    try:
        branch = db.query(Branch).filter( Branch.id == id ).first()
        branch.name = data.name

        db.add(branch)
        db.commit()
        db.refresh(branch)
        
        if branch is not None:
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
            branch = db.query(Branch).filter( Branch.id == i ).first() 
            db.delete(branch)
            db.commit()

        return HTTPException(status_code=status.HTTP_200_OK, detail='Success')
    except Exception as exc:
        print(exc)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='BAD REQUEST')