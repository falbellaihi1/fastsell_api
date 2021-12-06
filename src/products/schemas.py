from typing import List, Optional
from datetime import datetime
from enum import Enum
from pydantic import BaseModel


class type_of_product(str, Enum):
    car = "السيارات"


class city_list(str, Enum):
    car = "الرياض"


class Rate(BaseModel):
    rateValue: int
    seller: int
    comment: str

    class Config:
        orm_mode = True


class Product(BaseModel):
    id: int
    seller_id: int
    SKU: str
    product_name: str
    product_description: str
    category_id: int
    quantity: int
    unit_price: float
    MSRP: float
    color: str
    size: str
    unit_weight: float
    units_in_stock: int
    discounts_available: bool
    pictures: List

    class Config:
        orm_mode = True


class Seller(BaseModel):
    id: int
    seller_sub: str
    name: str
    company_name: str
    contact_name: str
    address: str
    city: str
    postal_code: str
    phone: str
    logo: str


class Category(BaseModel):
    id: int
    category_name: str
    description: str
    picture: str
    category_header_picture: str
    is_active: bool


class DeliverDriver(BaseModel):
    id: int
    driver_gov_id_type: str
    driver_gov_id: str
    driver_name: str
    driver_phone: str


class OrderDetails(BaseModel):
    id = int
    order_id: int
    product_id: int
    # order_number = Column(Integer, index=True)
    price: int
    quantity: int
    total: int
    color: str
    purchase_date: datetime


class Orders(BaseModel):
    id: int
    buyer_id: int
    payment_id: int
    driver_id: int
    purchase_date: datetime
    price: int
    quantity: int
    total: int
    color: int
    payment_date: datetime


class Payment(BaseModel):
    payment_id: int
    payment_type: str
    allowed: bool


class Buyer(BaseModel):
    id: int
    first_name: str
    last_name: str
    address: str
    city: str
    postal_code: str
    phone: str
    user_sub: str
