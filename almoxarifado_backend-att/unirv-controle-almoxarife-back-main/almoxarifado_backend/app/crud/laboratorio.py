from sqlalchemy.orm import Session
from app.models.laboratorio import Laboratorio
from app.schemas.laboratorio import LaboratorioCreate, LaboratorioUpdate

def get_laboratorio(db: Session, laboratorio_id: int):
    return db.query(Laboratorio).filter(Laboratorio.id == laboratorio_id).first()

def get_laboratorios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Laboratorio).offset(skip).limit(limit).all()

def create_laboratorio(db: Session, laboratorio: LaboratorioCreate):
    db_laboratorio = Laboratorio(**laboratorio.dict())
    db.add(db_laboratorio)
    db.commit()
    db.refresh(db_laboratorio)
    return db_laboratorio

def update_laboratorio(db: Session, laboratorio_id: int, laboratorio: LaboratorioUpdate):
    db_laboratorio = get_laboratorio(db, laboratorio_id)
    if db_laboratorio:
        for key, value in laboratorio.dict(exclude_unset=True).items():
            setattr(db_laboratorio, key, value)
        db.commit()
        db.refresh(db_laboratorio)
        return db_laboratorio
    return None

def delete_laboratorio(db: Session, laboratorio_id: int):
    db_laboratorio = get_laboratorio(db, laboratorio_id)
    if db_laboratorio:
        db.delete(db_laboratorio)
        db.commit()
        return db_laboratorio
    return None 