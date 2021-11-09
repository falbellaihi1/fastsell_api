from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, Request
from sqlalchemy.orm import Session
# import crud
from seller import models as sellerModels
from products import models as productModels
from products import schemas as productSchema
from seller import schemas as sellerSchema
from products import crud as productCrud
from seller import crud as sellerCrud
# from auth.auth import requires_auth
from database import SessionLocal, engine

sellerModels.Base.metadata.create_all(bind=engine)
productModels.Base.metadata.create_all(bind=engine)


app = FastAPI(title="fastsell")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/seller/name", response_model=sellerSchema.sellerBaselongResponse)
# @requires_auth('read:stylist')
def get_seller_by_name(seller: str, db: Session = Depends(get_db)):
    print('this is payload')
    return sellerCrud.get_seller_by_name(seller_name= seller)

# @app.get("/stylist/id",  response_model=schemas.StylistBaselongResponse)
# # @requires_auth('get:stylist')
# def get_stylist_by_id(stylist: int, db: Session = Depends(get_db)):
#     print(stylist)
#     return crud.get_stylist_by_id(db=db, stylist_id=stylist)

#
# @app.post("/stylist/", response_model=schemas.StylistMain)
# def create_stylist(stylist: schemas.StylistMain,
#                    db: Session = Depends(get_db)):
#     db_stylist = crud.create_stylist(db, stylist=stylist)
#     if db_stylist:
#         raise HTTPException(status_code=400,
#                             detail="stylist already registered")
#     return db_stylist
#
#
# @app.patch("/stylist/{stylist_id}", response_model=schemas.StylistMain)
# ## under construction
# async def update_stylist(stylist_id: int,stylist: schemas.StylistMain,
#                    db: Session = Depends(get_db)):
#     db_stylist = crud.update_stylist(db=db,stylist_id=stylist_id, stylist=stylist)
#     if db_stylist is None:
#         raise HTTPException(status_code=404,
#                             detail="stylist not found")
#
#     return db_stylist
#
#
# @app.get("/")
# @requires_auth('read:stylist')
# def read_root(request: Request, db: Session = Depends(get_db)):
#     return crud.get_stylist(db=db)
