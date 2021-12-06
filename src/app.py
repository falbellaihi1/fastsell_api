from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, Request
from sqlalchemy.orm import Session
# import crud
from products import models as productModels
from products import schemas as productSchema

from products import crud as productCrud

# from auth.auth import requires_auth
from database import SessionLocal, engine

productModels.Base.metadata.create_all(bind=engine)


app = FastAPI(title="fastsell")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()





# @app.get("/product/name", response_model=productSchema.ProductBaselongResponse)
# # @requires_auth('read:stylist')
# def get_seller_by_name(product: str, db: Session = Depends(get_db)):
#     print('this is payload')
#     return productCrud.get_product_by_name(db, product_name=product)

@app.get("/product/all")
# @requires_auth('read:stylist')
def get_products_all(db: Session = Depends(get_db)):
    print('this is payload')
    return productCrud.get_products(db)


@app.post("/product/create", response_model=productSchema.Product)
def create_product(product: productSchema.Product,
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
