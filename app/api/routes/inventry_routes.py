from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.inventry_schema import ItemCreate, ItemResponse, ItemUpdate , TotalValueResponse
from app.services.inventry_service import InventryService

router = APIRouter(prefix="/inventry", tags=["Inventry"])


@router.get("/", response_model=list[ItemResponse])
def get_items(db: Session = Depends(get_db)):
    return InventryService.get_items(db)

@router.get("/item/Value" , response_model=TotalValueResponse)
def get_all_values(db: Session = Depends(get_db)):
    return InventryService.get_total_value(db)

@router.get("/{item_id}", response_model=ItemResponse)
def get_item(item_id: int, db: Session = Depends(get_db)):
    return InventryService.get_item(db, item_id)

@router.post("/", response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    return InventryService.create_Item(db, item)

@router.put("/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: ItemUpdate, db: Session = Depends(get_db)):
    return InventryService.update_item(db, item_id, item)

@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    return InventryService.delete_item(db, item_id)

