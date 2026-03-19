from sqlalchemy.orm import Session
from app.repositories.inventry_repository import InventryRepository
from app.utils.exceptions import ItemNotFoundException

class InventryService:

    @staticmethod
    def create_Item(db: Session, item):
        return InventryRepository.create(db, item)

    @staticmethod
    def get_items(db: Session):
        return InventryRepository.get_all(db)

    @staticmethod
    def get_item(db: Session, item_id: int):
        item = InventryRepository.get_by_id(db,item_id)
        if not item:
            raise ItemNotFoundException("Item not found")
        return item

    @staticmethod
    def delete_item(db: Session, item_id: int):
        item = InventryRepository.delete(db, item_id)
        if not item:
            raise ItemNotFoundException("Item not found")
        return item
    
    @staticmethod
    def update_item(db: Session, item_id: int, item):
        updated_item = InventryRepository.update(db, item_id, item)
        if not updated_item:
            raise ItemNotFoundException("Item not found")
        return updated_item
    
    @staticmethod
    def get_total_value(db: Session):
        return InventryRepository.get_total_value(db)