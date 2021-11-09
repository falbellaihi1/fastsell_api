from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship
from database import Base

class Product(Base):
    __tablename__="product"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    image = Column(String, index=True)
    description = Column(String, index=True)
    type_product = Column(String, index=True)
    location = Column(String, index=True)
    range_price = Column(String, index=True)
    seller_id = Column(Integer, ForeignKey('seller.id'))
