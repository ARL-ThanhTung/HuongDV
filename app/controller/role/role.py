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


# Get All   Request  get_filter
@router.get(
    "/"
)
def get(
    db: Session = Depends(get_db)
):
    try:
        
        return 'aa'
    except Exception as exc:
        print(exc)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='BAD REQUEST')
