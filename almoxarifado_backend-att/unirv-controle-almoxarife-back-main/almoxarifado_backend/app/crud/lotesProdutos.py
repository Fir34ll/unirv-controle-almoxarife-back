from sqlalchemy.orm import Session
from app.models.lotesProdutos import LotesProdutos
from app.schemas.lotesProdutos import LotesProdutosCreate, LotesProdutosUpdate

def get_lote_produto(db: Session, lote_id: int):
    return db.query(LotesProdutos).filter(LotesProdutos.id == lote_id).first()

def get_lotes_produtos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(LotesProdutos).offset(skip).limit(limit).all()

def create_lote_produto(db: Session, lote: LotesProdutosCreate):
    db_lote = LotesProdutos(**lote.dict())
    db.add(db_lote)
    db.commit()
    db.refresh(db_lote)
    return db_lote

def update_lote_produto(db: Session, lote_id: int, lote: LotesProdutosUpdate):
    db_lote = get_lote_produto(db, lote_id)
    if db_lote:
        for key, value in lote.dict(exclude_unset=True).items():
            setattr(db_lote, key, value)
        db.commit()
        db.refresh(db_lote)
        return db_lote
    return None

def delete_lote_produto(db: Session, lote_id: int):
    db_lote = get_lote_produto(db, lote_id)
    if db_lote:
        db.delete(db_lote)
        db.commit()
        return db_lote
    return None 