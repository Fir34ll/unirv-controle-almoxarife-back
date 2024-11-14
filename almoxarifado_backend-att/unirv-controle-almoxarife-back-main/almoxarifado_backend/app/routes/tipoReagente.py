from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.tipoReagente import TipoReagente, TipoReagenteCreate, TipoReagenteUpdate
from app.crud.tipoReagente import get_tipo_reagente, get_tipos_reagente, create_tipo_reagente, update_tipo_reagente, delete_tipo_reagente

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/tipos-reagente/{tipo_reagente_id}", response_model=TipoReagente)
def read_tipo_reagente(tipo_reagente_id: int, db: Session = Depends(get_db)):
    db_tipo_reagente = get_tipo_reagente(db, tipo_reagente_id=tipo_reagente_id)
    if db_tipo_reagente is None:
        raise HTTPException(status_code=404, detail="Tipo de Reagente não encontrado")
    return db_tipo_reagente

@router.get("/tipos-reagente/", response_model=list[TipoReagente])
def read_tipos_reagente(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_tipos_reagente(db, skip=skip, limit=limit)

@router.post("/tipos-reagente/", response_model=TipoReagente)
def create_tipo_reagente_route(tipo_reagente: TipoReagenteCreate, db: Session = Depends(get_db)):
    return create_tipo_reagente(db=db, tipo_reagente=tipo_reagente)

@router.put("/tipos-reagente/{tipo_reagente_id}", response_model=TipoReagente)
def update_tipo_reagente_route(tipo_reagente_id: int, tipo_reagente: TipoReagenteUpdate, db: Session = Depends(get_db)):
    db_tipo_reagente = update_tipo_reagente(db, tipo_reagente_id, tipo_reagente)
    if db_tipo_reagente is None:
        raise HTTPException(status_code=404, detail="Tipo de Reagente não encontrado")
    return db_tipo_reagente

@router.delete("/tipos-reagente/{tipo_reagente_id}", response_model=TipoReagente)
def delete_tipo_reagente_route(tipo_reagente_id: int, db: Session = Depends(get_db)):
    db_tipo_reagente = delete_tipo_reagente(db, tipo_reagente_id)
    if db_tipo_reagente is None:
        raise HTTPException(status_code=404, detail="Tipo de Reagente não encontrado")
    return db_tipo_reagente 