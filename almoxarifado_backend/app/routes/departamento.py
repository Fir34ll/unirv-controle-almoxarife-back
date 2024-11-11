from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.crud.departamento import (
    get_departamento,
    get_departamentos,
    create_departamento,
    update_departamento,
    delete_departamento,
)
from app.schemas.departamento import Departamento, DepartamentoCreate, DepartamentoUpdate
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/departamentos/{departamento_id}", response_model=Departamento)
def read_departamento(departamento_id: int, db: Session = Depends(get_db)):
    db_departamento = get_departamento(db, departamento_id=departamento_id)
    if db_departamento is None:
        raise HTTPException(status_code=404, detail="Departamento não encontrado")
    return db_departamento

@router.get("/departamentos/", response_model=List[Departamento])
def read_departamentos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_departamentos(db, skip=skip, limit=limit)

@router.post("/departamentos/", response_model=Departamento)
def create_departamento_route(departamento: DepartamentoCreate, db: Session = Depends(get_db)):
    return create_departamento(db=db, departamento=departamento)

@router.put("/departamentos/{departamento_id}", response_model=Departamento)
def update_departamento_route(departamento_id: int, departamento: DepartamentoUpdate, db: Session = Depends(get_db)):
    db_departamento = update_departamento(db, departamento_id, departamento)
    if db_departamento is None:
        raise HTTPException(status_code=404, detail="Departamento não encontrado")
    return db_departamento

@router.delete("/departamentos/{departamento_id}", response_model=Departamento)
def delete_departamento_route(departamento_id: int, db: Session = Depends(get_db)):
    db_departamento = delete_departamento(db, departamento_id)
    if db_departamento is None:
        raise HTTPException(status_code=404, detail="Departamento não encontrado")
    return db_departamento
