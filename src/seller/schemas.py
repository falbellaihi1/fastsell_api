from typing import List, Optional
from enum import Enum
from pydantic import BaseModel

# class Rate(BaseModel):
#     rateValue:int
#     seller_id: int
#     comment:str
#     class Config:
#         orm_mode = True
class sellerMain(BaseModel):
    name: Optional[str] =""
    class Config:
        orm_mode = True

class update_seller(sellerMain):
    id: int
    name: str

class get_stylist(str):
    name:str
class sellerBaselongResponse(sellerMain):
    name: str =""
    class Config:
        orm_mode = True


