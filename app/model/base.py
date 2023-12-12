from sqlalchemy import Boolean, Column, ForeignKey, Integer, String , Float , Date
from sqlalchemy.orm import relationship

from app.db.base import Base


class Category(Base):
    __tablename__ = "Category"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String , nullable=True, default=None) 
    product = relationship("Product" , back_populates="category")

class Branch(Base):
    __tablename__ = "Branch"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String , nullable=True, default=None) 
    product = relationship("Product" , back_populates="branch")

class Product(Base):
    __tablename__ = "Product"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String , nullable=True, default=None) 
    image = Column(String , nullable=True, default=None) 
    description = Column(String , nullable=True, default=None) 
    category_id = Column(Integer,  ForeignKey("Category.id") ,  nullable=True, default=None )
    branch_id = Column(Integer,  ForeignKey("Branch.id") ,  nullable=True, default=None )

    category = relationship("Category" , back_populates="product")
    branch = relationship("Branch" , back_populates="product")
    product_detail = relationship("Product_Detail" , back_populates="product")

class Product_Detail(Base):
    __tablename__ = "Product_Detail"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    ram = Column(String , nullable=True, default=None) 
    rom = Column(String , nullable=True, default=None) 
    os = Column(String , nullable=True, default=None) 
    image = Column(String , nullable=True, default=None) 
    description = Column(String , nullable=True, default=None) 
    price = Column(Float, nullable=True, default=None)  
    camera = Column(String , nullable=True, default=None) 
    camera_self = Column(String , nullable=True, default=None) 
    battery = Column(Integer, nullable=True, default=None)  
    card = Column(String , nullable=True, default=None) 
    video = Column(String , nullable=True, default=None) 
    quantity_remain = Column(Integer, nullable=True, default=None)  
    chip = Column(String , nullable=True, default=None) 
    screen = Column(String , nullable=True, default=None) 
    product_id = Column(Integer,  ForeignKey("Product.id") ,  nullable=True, default=None )

    product = relationship("Product" , back_populates="product_detail")
    order_detail = relationship("Order_Detail" , back_populates="product_detail")

class Role(Base):
    __tablename__ = "Role"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String , nullable=True, default=None) 
    user = relationship("User" , back_populates="role")

class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    phone_number = Column(Integer, nullable=True, default=None)  
    password = Column(String , nullable=True, default=None) 
    full_name = Column(String , nullable=True, default=None) 
    address = Column(String , nullable=True, default=None) 
    email = Column(String , nullable=True, default=None) 
    role_id = Column(Integer,  ForeignKey("Role.id") ,  nullable=True, default=None )

    role = relationship("Role" , back_populates="user")
    order = relationship("Order" , back_populates="user")
    
class Order(Base):
    __tablename__ = "Order"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    total_amount = Column(Integer, nullable=True, default=None)  
    status = Column(Integer, nullable=True, default=None)  
    user_id = Column(Integer,  ForeignKey("User.id") ,  nullable=True, default=None )
    user = relationship("User" , back_populates="order")
    order_detail = relationship("Order_Detail" , back_populates="order")

class Order_Detail(Base):
    __tablename__ = "Order_Detail"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    quantity = Column(Integer, nullable=True, default=None)  
    into_money = Column(Float, nullable=True, default=None)  
    date = Column(Date, nullable=True, default=None)  
    order_id = Column(Integer,  ForeignKey("Order.id") ,  nullable=True, default=None )
    product_detail_id = Column(Integer,  ForeignKey("Product_Detail.id") ,  nullable=True, default=None )   

    order = relationship("Order" , back_populates="order_detail")
    product_detail = relationship("Product_Detail" , back_populates="order_detail")


