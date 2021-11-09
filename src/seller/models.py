from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship
from database import Base

class seller(Base):
    __tablename__="seller"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)


class sellerProducts(Base):
    __tablename__ ="sellerProducts"
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'))
    seller_id = Column(Integer, ForeignKey('seller.id'))




