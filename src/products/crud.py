from sqlalchemy.orm import Session

import products.models as models
import products.schemas as schemas


# def get_product_by_id(db: Session, product_id: int):
#     return db.query(models.Product).filter(
#         models.Product.id == product_id).first()


# def get_product_by_name(db: Session, product_name: str):
#     return db.query(models.Product).filter(
#         models.Product.name == product_name).first()


def create_product(db: Session, product: schemas.Product):
    db_prouct = models.Products(id=product.id,
                                seller_id=product.seller_id,
                                SKU=product.SKU,
                                product_name=product.product_name,
                                product_description=product.product_description,
                                category_id=product.category_id,
                                quantity=product.quantity,
                                unit_price=product.unit_price,
                                MSRP=product.MSRP,
                                color=product.color,
                                size=product.size,
                                unit_weight=product.unit_weight,
                                units_in_stock=product.units_in_stock,
                                discounts_available=product.discounts_available,
                                pictures=product.pictures

                                )
    db.add(db_prouct)
    db.commit()
    db.refresh(db_prouct)
    return db_prouct


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Products).offset(skip).limit(limit).all()


# def update_stylist(db: Session, stylist_id:int ,stylist: schemas.StylistMain):
#     db_stylist = db.query(models.Stylist).filter(models.Stylist.id ==stylist_id ).first()
#     db_stylist.name = stylist.name
#     db_stylist.bio = stylist.bio
#     db_stylist.city = stylist.city
#     db_stylist.can_travel = stylist.can_travel
#     db_stylist.experience = stylist.experience
#     db_stylist.certificates = stylist.certificates
#     db_stylist.does_training = stylist.does_training
#     db_stylist.range_price = stylist.range_price
#     db_stylist.type_artist = stylist.type_artist
#     db.commit()
#     db.refresh(db_stylist)
#     return db_stylist
#
#
# def delete_stylist(db: Session, stylist_id: int):
#     db_stylist = db.query(models.Stylist).filter(models.Stylist.id == stylist_id).first()
#     db.delete(db_stylist)
#     db.commit()
#     return db_stylist


# def get_stylist(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Stylist).offset(skip).limit(limit).all()
