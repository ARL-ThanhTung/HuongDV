from fastapi import APIRouter

from app.controller.category import category 
from app.controller.branch import branch 
from app.controller.product import product 
from app.controller.product_detail import product_detail 
from app.controller.role import role 
from app.controller.user import user 
from app.controller.order import order 
from app.controller.order_detail import order_detail 

router = APIRouter()

# user 
router.include_router(category.router, tags=["category"], prefix="/category")
router.include_router(branch.router, tags=["branch"], prefix="/branch")
router.include_router(product.router, tags=["product"], prefix="/product")
router.include_router(product_detail.router, tags=["product_detail"], prefix="/product_detail")
# router.include_router(role.router, tags=["role"], prefix="/role")
# router.include_router(user.router, tags=["user"], prefix="/user")
# router.include_router(order.router, tags=["order"], prefix="/order")  
# router.include_router(order_detail.router, tags=["order_detail"], prefix="/order_detail")

