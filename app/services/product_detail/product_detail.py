from fastapi import Depends
from fastapi_sqlalchemy import db

from fastapi import HTTPException
from sqlalchemy import or_
from typing import List
from sqlalchemy import and_
from app.db.base import get_db
from sqlalchemy.orm import Session

from app.model.base import Product_Detail
from app.schema.product_detail.product_detail import ProductDetailRequest


class ProductDetailService(object):
    __instance = None 

    @staticmethod
    def createProductDetail( data: ProductDetailRequest , db: Session = Depends(get_db) ):  
        res = Product_Detail(**data.dict())
        db.add(res)
        db.commit()
        db.refresh(res)
        return res 