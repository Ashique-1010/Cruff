from sqlalchemy.orm import Session
from app.models.item import Item
from app.schemas.item import ItemCreate

def get_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Item).offset(skip).limit(limit).all()

def get_item( item_id: int, db: Session):
    return db.query(Item).filter(Item.id==item_id).first()

def create_item( item: ItemCreate, db: Session):
    db_item = Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_item(item_id: int, db: Session):
    db_item = db.query(Item).filter(Item.id==item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item