from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship
from database import Base


class Make(Base):
    __tablename__ = "make"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    image = Column(String)#string of the image route


class Model(Base):
    __tablename__ = "model"
    id = Column(Integer, primary_key=True, index=True)
    make_id = Column(Integer, ForeignKey('make.id'))
    name = Column(String)
    image = Column(String)  # string of the image route



class Year(Base):
    __tablename__ = "year"
    id = Column(Integer, primary_key=True, index=True)
    car_model_id = Column(Integer, ForeignKey('model.id'))
    date_year = Column(String)




class Trim(Base):
    __tablename__ = "trim"
    id = Column(Integer, primary_key=True, index=True)
    car_model_id = Column(Integer, ForeignKey('model.id'))
    car_make_id = Column(Integer, ForeignKey('make.id'))
    name = Column(String)
    car_year = Column(String)
