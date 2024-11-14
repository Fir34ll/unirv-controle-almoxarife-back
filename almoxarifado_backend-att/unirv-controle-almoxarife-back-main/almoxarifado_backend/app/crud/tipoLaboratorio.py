from sqlalchemy.orm import Session
from app.models.tipoLaboratorio import TipoLaboratorio
from app.schemas.tipoLaboratorio import TipoLaboratorioCreate, TipoLaboratorioUpdate

def get_tipo_laboratorio(db: Session, tipo_laboratorio_id: int):
    return db.query(TipoLaboratorio).filter(TipoLaboratorio.id == tipo_laboratorio_id).first()

def get_tipos_laboratorio(db: Session, skip: int = 0, limit: int = 10):
    return db.query(TipoLaboratorio).offset(skip).limit(limit).all()

def create_tipo_laboratorio(db: Session, tipo_laboratorio: TipoLaboratorioCreate):
    db_tipo_laboratorio = TipoLaboratorio(**tipo_laboratorio.dict())
    db.add(db_tipo_laboratorio)
    db.commit()
    db.refresh(db_tipo_laboratorio)
    return db_tipo_laboratorio

def update_tipo_laboratorio(db: Session, tipo_laboratorio_id: int, tipo_laboratorio: TipoLaboratorioUpdate):
    db_tipo_laboratorio = get_tipo_laboratorio(db, tipo_laboratorio_id)
    if db_tipo_laboratorio:
        for key, value in tipo_laboratorio.dict(exclude_unset=True).items():
            setattr(db_tipo_laboratorio, key, value)
        db.commit()
        db.refresh(db_tipo_laboratorio)
        return db_tipo_laboratorio
    return None

def delete_tipo_laboratorio(db: Session, tipo_laboratorio_id: int):
    db_tipo_laboratorio = get_tipo_laboratorio(db, tipo_laboratorio_id)
    if db_tipo_laboratorio:
        db.delete(db_tipo_laboratorio)
        db.commit()
        return db_tipo_laboratorio
    return None 