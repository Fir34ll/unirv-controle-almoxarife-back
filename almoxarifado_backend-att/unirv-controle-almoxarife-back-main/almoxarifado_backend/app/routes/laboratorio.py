from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.laboratorio import Laboratorio, LaboratorioCreate, LaboratorioUpdate
from app.crud.laboratorio import get_laboratorio, get_laboratorios, create_laboratorio, update_laboratorio, delete_laboratorio

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/laboratorios/{laboratorio_id}", response_model=Laboratorio)
def read_laboratorio(laboratorio_id: int, db: Session = Depends(get_db)):
    db_laboratorio = get_laboratorio(db, laboratorio_id=laboratorio_id)
    if db_laboratorio is None:
        raise HTTPException(status_code=404, detail="Laboratório não encontrado")
    return db_laboratorio

@router.get("/laboratorios/", response_model=list[Laboratorio])
def read_laboratorios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_laboratorios(db, skip=skip, limit=limit)

@router.post("/laboratorios/", response_model=Laboratorio)
def create_laboratorio_route(laboratorio: LaboratorioCreate, db: Session = Depends(get_db)):
    return create_laboratorio(db=db, laboratorio=laboratorio)

@router.put("/laboratorios/{laboratorio_id}", response_model=Laboratorio)
def update_laboratorio_route(laboratorio_id: int, laboratorio: LaboratorioUpdate, db: Session = Depends(get_db)):
    db_laboratorio = update_laboratorio(db, laboratorio_id, laboratorio)
    if db_laboratorio is None:
        raise HTTPException(status_code=404, detail="Laboratório não encontrado")
    return db_laboratorio

@router.delete("/laboratorios/{laboratorio_id}", response_model=Laboratorio)
def delete_laboratorio_route(laboratorio_id: int, db: Session = Depends(get_db)):
    db_laboratorio = delete_laboratorio(db, laboratorio_id)
    if db_laboratorio is None:
        raise HTTPException(status_code=404, detail="Laboratório não encontrado")
    return db_laboratorio 