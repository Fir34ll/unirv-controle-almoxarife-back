from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.itemLaboratorio import ItemLaboratorio, ItemLaboratorioCreate
from app.crud.itemLaboratorio import get_item_laboratorio, get_items_laboratorio, create_item_laboratorio, delete_item_laboratorio

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/item-laboratorios/{item_laboratorio_id}", response_model=ItemLaboratorio)
def read_item_laboratorio(item_laboratorio_id: int, db: Session = Depends(get_db)):
    db_item_laboratorio = get_item_laboratorio(db, item_laboratorio_id=item_laboratorio_id)
    if db_item_laboratorio is None:
        raise HTTPException(status_code=404, detail="Item de Laboratório não encontrado")
    return db_item_laboratorio

@router.get("/item-laboratorios/", response_model=list[ItemLaboratorio])
def read_items_laboratorio(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_items_laboratorio(db, skip=skip, limit=limit)

@router.post("/item-laboratorios/", response_model=ItemLaboratorio)
def create_item_laboratorio_route(item_laboratorio: ItemLaboratorioCreate, db: Session = Depends(get_db)):
    return create_item_laboratorio(db=db, item_laboratorio=item_laboratorio)

@router.delete("/item-laboratorios/{item_laboratorio_id}", response_model=ItemLaboratorio)
def delete_item_laboratorio_route(item_laboratorio_id: int, db: Session = Depends(get_db)):
    db_item_laboratorio = delete_item_laboratorio(db, item_laboratorio_id)
    if db_item_laboratorio is None:
        raise HTTPException(status_code=404, detail="Item de Laboratório não encontrado")
    return db_item_laboratorio 