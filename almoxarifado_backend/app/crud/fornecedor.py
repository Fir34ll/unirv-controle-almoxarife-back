# app/crud/fornecedor.py

from sqlalchemy.orm import Session
from app.models.fornecedor import Fornecedor
from app.schemas.fornecedor import FornecedorCreate, FornecedorUpdate

def get_fornecedor(db: Session, fornecedor_id: int):
    return db.query(Fornecedor).filter(Fornecedor.id == fornecedor_id).first()

def get_fornecedores(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Fornecedor).offset(skip).limit(limit).all()

def create_fornecedor(db: Session, fornecedor: FornecedorCreate):
    db_fornecedor = Fornecedor(**fornecedor.dict())
    db.add(db_fornecedor)
    db.commit()
    db.refresh(db_fornecedor)
    return db_fornecedor

def update_fornecedor(db: Session, fornecedor_id: int, fornecedor: FornecedorUpdate):
    db_fornecedor = get_fornecedor(db, fornecedor_id)
    if db_fornecedor:
        for key, value in fornecedor.dict(exclude_unset=True).items():
            setattr(db_fornecedor, key, value)
        db.commit()
        db.refresh(db_fornecedor)
        return db_fornecedor
    return None

def delete_fornecedor(db: Session, fornecedor_id: int):
    db_fornecedor = get_fornecedor(db, fornecedor_id)
    if db_fornecedor:
        db.delete(db_fornecedor)
        db.commit()
        return db_fornecedor
    return None
