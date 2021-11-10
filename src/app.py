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
    return sellerCrud.get_seller_by_name(db,seller_name= seller)

@app.post("/seller/", response_model=sellerSchema.sellerMain)
def create_stylist(seller: sellerSchema.sellerMain,
                   db: Session = Depends(get_db)):
    db_seller = sellerCrud.create_seller(db, seller=seller)
    if db_seller:
        raise HTTPException(status_code=400,
                            detail="seller already registered")
    return db_seller




@app.get("/product/name", response_model=productSchema.ProductBaselongResponse)
# @requires_auth('read:stylist')
def get_seller_by_name(product: str, db: Session = Depends(get_db)):
    print('this is payload')
    return productCrud.get_product_by_name(db, product_name=product)


@app.post("/product/create", response_model=productSchema.productMain)
def create_stylist(product: productSchema.productMain,
                   db: Session = Depends(get_db)):
    db_product = productCrud.create_product(db, product=product)
    # if db_product:
    #     raise HTTPException(status_code=400,
    #                         detail="seller already registered")
    return db_product
# @app.get("/stylist/id",  response_model=schemas.StylistBaselongResponse)
# # @requires_auth('get:stylist')
# def get_stylist_by_id(stylist: int, db: Session = Depends(get_db)):
#     print(stylist)
#     return crud.get_stylist_by_id(db=db, stylist_id=stylist)

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
