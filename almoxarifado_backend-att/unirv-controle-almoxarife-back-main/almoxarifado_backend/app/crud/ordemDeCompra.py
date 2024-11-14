from sqlalchemy.orm import Session
from app.models.ordemDeCompra import OrdemDeCompra
from app.schemas.ordemDeCompra import OrdemDeCompraCreate, OrdemDeCompraUpdate

def get_ordem_de_compra(db: Session, ordem_id: int):
    return db.query(OrdemDeCompra).filter(OrdemDeCompra.id == ordem_id).first()

def get_ordens_de_compra(db: Session, skip: int = 0, limit: int = 10):
    return db.query(OrdemDeCompra).offset(skip).limit(limit).all()

def create_ordem_de_compra(db: Session, ordem: OrdemDeCompraCreate):
    db_ordem = OrdemDeCompra(**ordem.dict())
    db.add(db_ordem)
    db.commit()
    db.refresh(db_ordem)
    return db_ordem

def update_ordem_de_compra(db: Session, ordem_id: int, ordem: OrdemDeCompraUpdate):
    db_ordem = get_ordem_de_compra(db, ordem_id)
    if db_ordem:
        for key, value in ordem.dict(exclude_unset=True).items():
            setattr(db_ordem, key, value)
        db.commit()
        db.refresh(db_ordem)
        return db_ordem
    return None

def delete_ordem_de_compra(db: Session, ordem_id: int):
    db_ordem = get_ordem_de_compra(db, ordem_id)
    if db_ordem:
        db.delete(db_ordem)
        db.commit()
        return db_ordem
    return None
