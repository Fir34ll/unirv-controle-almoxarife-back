from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.unidadeDeMedida import UnidadeDeMedida, UnidadeDeMedidaCreate, UnidadeDeMedidaUpdate
from app.crud.unidadeDeMedida import get_unidade_de_medida, get_unidades_de_medida, create_unidade_de_medida, update_unidade_de_medida, delete_unidade_de_medida

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/unidades-de-medida/{unidade_id}", response_model=UnidadeDeMedida)
def read_unidade_de_medida(unidade_id: int, db: Session = Depends(get_db)):
    db_unidade = get_unidade_de_medida(db, unidade_id=unidade_id)
    if db_unidade is None:
        raise HTTPException(status_code=404, detail="Unidade de Medida não encontrada")
    return db_unidade

@router.get("/unidades-de-medida/", response_model=list[UnidadeDeMedida])
def read_unidades_de_medida(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_unidades_de_medida(db, skip=skip, limit=limit)

@router.post("/unidades-de-medida/", response_model=UnidadeDeMedida)
def create_unidade_de_medida_route(unidade: UnidadeDeMedidaCreate, db: Session = Depends(get_db)):
    return create_unidade_de_medida(db=db, unidade=unidade)

@router.put("/unidades-de-medida/{unidade_id}", response_model=UnidadeDeMedida)
def update_unidade_de_medida_route(unidade_id: int, unidade: UnidadeDeMedidaUpdate, db: Session = Depends(get_db)):
    db_unidade = update_unidade_de_medida(db, unidade_id, unidade)
    if db_unidade is None:
        raise HTTPException(status_code=404, detail="Unidade de Medida não encontrada")
    return db_unidade

@router.delete("/unidades-de-medida/{unidade_id}", response_model=UnidadeDeMedida)
def delete_unidade_de_medida_route(unidade_id: int, db: Session = Depends(get_db)):
    db_unidade = delete_unidade_de_medida(db, unidade_id)
    if db_unidade is None:
        raise HTTPException(status_code=404, detail="Unidade de Medida não encontrada")
    return db_unidade 