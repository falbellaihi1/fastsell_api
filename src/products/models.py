from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship
from database import Base


class Seller(Base):
    __tablename__ = "seller"
    id = Column(Integer, primary_key=True, index=True)
    seller_sub = Column(String, index=True)
    name = Column(String, index=True)
    company_name = Column(String, index=True)
    contact_name = Column(String, index=True)
    address = Column(String, index=True)
    city = Column(String, index=True)
    postal_code = Column(String, index=True)
    phone = Column(String, index=True)
    logo = Column(String, index=True)
    user_sub = Column(String, index=True)  # jwt id this is to identify user with auth0 or whatever


class DeliverDriver(Base):
    __tablename__ = "driver"
    id = Column(Integer, primary_key=True)
    driver_gov_id_type = Column(String, index=True)
    driver_gov_id = Column(String, index=True)
    driver_name = Column(String, index=True)
    driver_phone = Column(String, index=True)
    user_sub = Column(String, index=True)  # jwt id this is to identify user with auth0 or whatever


class Buyer(Base):
    __tablename__ = 'buyer'
    id = Column(Integer, primary_key=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    address = Column(String, index=True)
    city = Column(String, index=True)
    postal_code = Column(String, index=True)
    phone = Column(String, index=True)
    user_sub = Column(String, index=True)  # jwt id this is to identify user with auth0 or whatever


class Products(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    seller_id = Column(Integer, ForeignKey('seller.id'))
    SKU = Column(String, index=True)
    product_name = Column(String, index=True)
    product_description = Column(String, index=True)
    category_id = Column(Integer, ForeignKey('category.id'))
    quantity = Column(Integer, index=True)
    unit_price = Column(Float, index=True)
    MSRP = Column(Float, index=True)
    color = Column(String, index=True)
    size = Column(String, index=True)
    unit_weight = Column(Float, index=True)
    units_in_stock = Column(Integer, index=True)
    discounts_available = Column(Boolean, index=True)
    pictures = Column(ARRAY(String), index=True)


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True)
    category_name = Column(String, index=True)
    description = Column(String, index=True)
    picture = Column(String, index=True)
    category_header_picture = Column(String, index=True)
    is_active = Column(Boolean, index=True)


class OrderDetails(Base):
    __tablename__ = "order_details"
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    # order_number = Column(Integer, index=True)
    price = Column(Integer, index=True)
    quantity = Column(Integer, index=True)
    total = Column(Integer, index=True)
    color = Column(String, index=True)
    purchase_date = Column(DateTime, index=True)


class Orders(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    buyer_id = Column(Integer, ForeignKey('buyer.id'))
    payment_id = Column(Integer, ForeignKey('payment.id'))
    driver_id = Column(Integer, ForeignKey('driver.id'))
    purchase_date = Column(DateTime)
    # order_number = Column(Integer)
    price = Column(Integer)
    quantity = Column(Integer, index=True)
    total = Column(Integer, index=True)
    color = Column(String, index=True)
    payment_date = Column(DateTime)


class Payment(Base):
    __tablename__ = "payment"
    id = Column(Integer, primary_key=True)
    payment_type = Column(String, index=True)
    allowed = Column(Boolean)
