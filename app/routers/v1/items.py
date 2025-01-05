from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import get_db 
from app.schemas.item import Item as item_schema, ItemCreate
from app.models.item import Item as item_model
from app.services.item_service import get_items, get_item, create_item, delete_item

item_router = APIRouter(
    prefix="/items",
    tags="items"
)

@item_router.get("/", response_model=list[item_schema])
def show_it(db: Session = Depends(get_db)):
    items = get_items(db)

@item_router.post("/", response_model=item_schema)
def create_it(item: ItemCreate, db: Session = Depends(get_db)):
    return create_item(item, db)

@item_router.get("/{id}", response_model=item_schema)
def find_it(id: int, db: Session = Depends(get_db)):
    item = get_item(id, db)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@item_router.delete("/{id}", response_model=item_schema)
def delete_it(id: int, db: Session = Depends(get_db)):
    item = delete_item(id, db)
    if not item:
        raise HTTPException(status_code=404, detail="Item to delete not found")
    return item