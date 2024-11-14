from sqlalchemy.orm import Session
from app.models.tipoReagente import TipoReagente
from app.schemas.tipoReagente import TipoReagenteCreate, TipoReagenteUpdate

def get_tipo_reagente(db: Session, tipo_reagente_id: int):
    return db.query(TipoReagente).filter(TipoReagente.id == tipo_reagente_id).first()

def get_tipos_reagente(db: Session, skip: int = 0, limit: int = 10):
    return db.query(TipoReagente).offset(skip).limit(limit).all()

def create_tipo_reagente(db: Session, tipo_reagente: TipoReagenteCreate):
    db_tipo_reagente = TipoReagente(**tipo_reagente.dict())
    db.add(db_tipo_reagente)
    db.commit()
    db.refresh(db_tipo_reagente)
    return db_tipo_reagente

def update_tipo_reagente(db: Session, tipo_reagente_id: int, tipo_reagente: TipoReagenteUpdate):
    db_tipo_reagente = get_tipo_reagente(db, tipo_reagente_id)
    if db_tipo_reagente:
        for key, value in tipo_reagente.dict(exclude_unset=True).items():
            setattr(db_tipo_reagente, key, value)
        db.commit()
        db.refresh(db_tipo_reagente)
        return db_tipo_reagente
    return None

def delete_tipo_reagente(db: Session, tipo_reagente_id: int):
    db_tipo_reagente = get_tipo_reagente(db, tipo_reagente_id)
    if db_tipo_reagente:
        db.delete(db_tipo_reagente)
        db.commit()
        return db_tipo_reagente
    return None 