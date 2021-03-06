from typing import List, Optional
from datetime import datetime
from enum import Enum
from pydantic import BaseModel


class Make(BaseModel):
    id:int
    name:str
    image:str
    class Config:
        orm_mode = True


class Model(BaseModel):
    id: int
    make_int:int
    name: str
    image: str
    class Config:
        orm_mode = True

class Year(BaseModel):
    id: int
    date_year:str
    class Config:
        orm_mode = True

class Tirm(BaseModel):
    id:int
    car_model_id:int
    car_make_id:int
    name:str
    car_year:str


