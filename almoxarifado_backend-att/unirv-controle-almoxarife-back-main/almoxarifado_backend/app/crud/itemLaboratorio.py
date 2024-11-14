from sqlalchemy.orm import Session
from app.models.itemLaboratorio import ItemLaboratorio
from app.schemas.itemLaboratorio import ItemLaboratorioCreate

def get_item_laboratorio(db: Session, item_laboratorio_id: int):
    return db.query(ItemLaboratorio).filter(ItemLaboratorio.id == item_laboratorio_id).first()

def get_items_laboratorio(db: Session, skip: int = 0, limit: int = 10):
    return db.query(ItemLaboratorio).offset(skip).limit(limit).all()

def create_item_laboratorio(db: Session, item_laboratorio: ItemLaboratorioCreate):
    db_item_laboratorio = ItemLaboratorio(**item_laboratorio.dict())
    db.add(db_item_laboratorio)
    db.commit()
    db.refresh(db_item_laboratorio)
    return db_item_laboratorio

def delete_item_laboratorio(db: Session, item_laboratorio_id: int):
    db_item_laboratorio = get_item_laboratorio(db, item_laboratorio_id)
    if db_item_laboratorio:
        db.delete(db_item_laboratorio)
        db.commit()
        return db_item_laboratorio
    return None 