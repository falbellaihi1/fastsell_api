from sqlalchemy.orm import Session

import seller.models as models
import seller.schemas as schemas


def get_seller_by_id(db: Session, seller_id: int):
    return db.query(models.seller).filter(
        models.seller.id == seller_id).first()


def get_seller_by_name(db: Session, seller_name: str):
    return db.query(models.seller).filter(
        models.seller.name == seller_name).first()


def create_seller(db: Session, seller: schemas.sellerMain):
    seller = models.seller(name=seller.name)
    db.add(seller)
    db.commit()
    db.refresh(seller)
    return seller


def update_stylist(db: Session, seller_id: int, seller: schemas.sellerMain):
    db = db.query(models.seller).filter(models.seller.id == seller_id).first()
    seller.name = seller.name
    db.commit()
    db.refresh(seller)
    return seller

# def delete_stylist(db: Session, stylist_id: int):
#     db_stylist = db.query(models.Stylist).filter(models.Stylist.id == stylist_id).first()
#     db.delete(db_stylist)
#     db.commit()
#     return db_stylist


#
# def get_stylist(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Stylist).offset(skip).limit(limit).all()
