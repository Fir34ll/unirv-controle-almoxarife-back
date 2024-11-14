from sqlalchemy.orm import Session
from app.models.departamento import Departamento
from app.schemas.departamento import DepartamentoCreate, DepartamentoUpdate

def get_departamento(db: Session, departamento_id: int):
    return db.query(Departamento).filter(Departamento.id == departamento_id).first()

def get_departamentos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Departamento).offset(skip).limit(limit).all()

def create_departamento(db: Session, departamento: DepartamentoCreate):
    db_departamento = Departamento(**departamento.dict())
    db.add(db_departamento)
    db.commit()
    db.refresh(db_departamento)
    return db_departamento

def update_departamento(db: Session, departamento_id: int, departamento: DepartamentoUpdate):
    db_departamento = get_departamento(db, departamento_id)
    if db_departamento:
        for key, value in departamento.dict(exclude_unset=True).items():
            setattr(db_departamento, key, value)
        db.commit()
        db.refresh(db_departamento)
    return db_departamento

def delete_departamento(db: Session, departamento_id: int):
    db_departamento = get_departamento(db, departamento_id)
    if db_departamento:
        db.delete(db_departamento)
        db.commit()
    return db_departamento
