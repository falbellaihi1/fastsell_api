from typing import List, Optional
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


class productMain(BaseModel):
    name: Optional[str] = ""
    image:Optional[str]=""
    description: Optional[str] = ""
    type_product: Optional[List[type_of_product]] = None
    location: Optional[List[city_list]] = None
    range_price: Optional[str] = ""

    class Config:
        orm_mode = True


class update_stylist(productMain):
    name: Optional[str] = ""
    description: Optional[str] = ""
    type_product: Optional[List[type_of_product]] = None
    city: Optional[List[city_list]] = None
    range_price: Optional[str] = ""
    # id: int
    # name: str
    # experience: int
    # certificates: str
    # does_training: bool
    # bio: str
    # type_artist: List[type_art]
    # city:str
    # can_travel:bool
    # range_price:str


class get_product(str):
    name: str


class ProductBaselongResponse(productMain):
    name: Optional[str] = ""
    description: Optional[str] = ""
    type_product: Optional[List[type_of_product]] = None
    city: Optional[List[city_list]] = None
    range_price: Optional[str] = ""

    # name: str =""
    # experience: int =0
    # certificates: str =""
    # does_training: bool =False
    # bio: str =""
    # type_artist: List[type_art]=None
    # city:str =""
    # can_travel:bool=False
    # range_price:str =""
    class Config:
        orm_mode = True
