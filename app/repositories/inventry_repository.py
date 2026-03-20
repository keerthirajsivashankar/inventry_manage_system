from sqlalchemy.orm import Session
from app.models.inventry_model import Inventry
from app.core.logger import logger

class InventryRepository:

    @staticmethod
    def get_all(db: Session):
        logger.info("Fetching all Items")
        return db.query(Inventry).all()

    @staticmethod
    def get_by_id(db: Session, Item_id: int):
        logger.info(f"Fetching item with ID: {Item_id}")
        return db.query(Inventry).filter(Inventry.id == Item_id).first()
    
    @staticmethod
    def get_total_value(db: Session):
        logger.info("Fetching total item value")
        items = db.query(Inventry.qty, Inventry.price).all()
        total_value = sum((quantity or 0) * (price or 0) for quantity, price in items)
        return {"total_value": total_value}

    @staticmethod
    def create(db: Session, item):
        db_item = Inventry(name=item.name,price=item.price,qty=item.qty,description=item.description)
        db.add(db_item)
        logger.info(f"Creating item: {item.name}")
        db.commit()
        db.refresh(db_item)
        return db_item

    @staticmethod
    def update(db: Session, Item_id: int, item):
        logger.info(f"Updating item with ID: {Item_id}")
        db_item = db.query(Inventry).filter(Inventry.id == Item_id).first()
        if db_item:
            db_item.name = item.name if item.name is not None else db_item.name
            db_item.price = item.price if item.price is not None else db_item.price
            db_item.qty = item.qty if item.qty is not None else db_item.qty
            db_item.description = item.description if item.description is not None else db_item.description
            db.commit()
            db.refresh(db_item)
        return db_item

    @staticmethod
    def delete(db: Session, Item_id: int):
        logger.info(f"Deleting item with ID: {Item_id}")
        item = db.query(Inventry).filter(Inventry.id == Item_id).first()
        if item:
            db.delete(item)
            db.commit()
        return item
    
    
    

    