from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.tipoLaboratorio import TipoLaboratorio, TipoLaboratorioCreate, TipoLaboratorioUpdate
from app.crud.tipoLaboratorio import get_tipo_laboratorio, get_tipos_laboratorio, create_tipo_laboratorio, update_tipo_laboratorio, delete_tipo_laboratorio

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/tipos-laboratorio/{tipo_laboratorio_id}", response_model=TipoLaboratorio)
def read_tipo_laboratorio(tipo_laboratorio_id: int, db: Session = Depends(get_db)):
    db_tipo_laboratorio = get_tipo_laboratorio(db, tipo_laboratorio_id=tipo_laboratorio_id)
    if db_tipo_laboratorio is None:
        raise HTTPException(status_code=404, detail="Tipo de Laboratório não encontrado")
    return db_tipo_laboratorio

@router.get("/tipos-laboratorio/", response_model=list[TipoLaboratorio])
def read_tipos_laboratorio(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_tipos_laboratorio(db, skip=skip, limit=limit)

@router.post("/tipos-laboratorio/", response_model=TipoLaboratorio)
def create_tipo_laboratorio_route(tipo_laboratorio: TipoLaboratorioCreate, db: Session = Depends(get_db)):
    return create_tipo_laboratorio(db=db, tipo_laboratorio=tipo_laboratorio)

@router.put("/tipos-laboratorio/{tipo_laboratorio_id}", response_model=TipoLaboratorio)
def update_tipo_laboratorio_route(tipo_laboratorio_id: int, tipo_laboratorio: TipoLaboratorioUpdate, db: Session = Depends(get_db)):
    db_tipo_laboratorio = update_tipo_laboratorio(db, tipo_laboratorio_id, tipo_laboratorio)
    if db_tipo_laboratorio is None:
        raise HTTPException(status_code=404, detail="Tipo de Laboratório não encontrado")
    return db_tipo_laboratorio

@router.delete("/tipos-laboratorio/{tipo_laboratorio_id}", response_model=TipoLaboratorio)
def delete_tipo_laboratorio_route(tipo_laboratorio_id: int, db: Session = Depends(get_db)):
    db_tipo_laboratorio = delete_tipo_laboratorio(db, tipo_laboratorio_id)
    if db_tipo_laboratorio is None:
        raise HTTPException(status_code=404, detail="Tipo de Laboratório não encontrado")
    return db_tipo_laboratorio 