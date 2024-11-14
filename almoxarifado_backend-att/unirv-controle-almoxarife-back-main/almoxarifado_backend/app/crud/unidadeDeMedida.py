from sqlalchemy.orm import Session
from app.models.unidadeDeMedida import UnidadeDeMedida
from app.schemas.unidadeDeMedida import UnidadeDeMedidaCreate, UnidadeDeMedidaUpdate

def get_unidade_de_medida(db: Session, unidade_id: int):
    return db.query(UnidadeDeMedida).filter(UnidadeDeMedida.id == unidade_id).first()

def get_unidades_de_medida(db: Session, skip: int = 0, limit: int = 10):
    return db.query(UnidadeDeMedida).offset(skip).limit(limit).all()

def create_unidade_de_medida(db: Session, unidade: UnidadeDeMedidaCreate):
    db_unidade = UnidadeDeMedida(**unidade.dict())
    db.add(db_unidade)
    db.commit()
    db.refresh(db_unidade)
    return db_unidade

def update_unidade_de_medida(db: Session, unidade_id: int, unidade: UnidadeDeMedidaUpdate):
    db_unidade = get_unidade_de_medida(db, unidade_id)
    if db_unidade:
        for key, value in unidade.dict(exclude_unset=True).items():
            setattr(db_unidade, key, value)
        db.commit()
        db.refresh(db_unidade)
        return db_unidade
    return None

def delete_unidade_de_medida(db: Session, unidade_id: int):
    db_unidade = get_unidade_de_medida(db, unidade_id)
    if db_unidade:
        db.delete(db_unidade)
        db.commit()
        return db_unidade
    return None 