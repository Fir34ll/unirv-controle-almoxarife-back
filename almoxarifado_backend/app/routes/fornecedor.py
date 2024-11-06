from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.fornecedor import Fornecedor, FornecedorCreate, FornecedorUpdate
from app.crud.fornecedor import get_fornecedor, get_fornecedores, create_fornecedor, update_fornecedor, delete_fornecedor

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/fornecedores/{fornecedor_id}", response_model=Fornecedor)
def read_fornecedor(fornecedor_id: int, db: Session = Depends(get_db)):
    db_fornecedor = get_fornecedor(db, fornecedor_id=fornecedor_id)
    if db_fornecedor is None:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    return db_fornecedor

@router.get("/fornecedores/", response_model=list[Fornecedor])
def read_fornecedores(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_fornecedores(db, skip=skip, limit=limit)

@router.post("/fornecedores/", response_model=Fornecedor)
def create_fornecedor_route(fornecedor: FornecedorCreate, db: Session = Depends(get_db)):
    return create_fornecedor(db=db, fornecedor=fornecedor)

@router.put("/fornecedores/{fornecedor_id}", response_model=Fornecedor)
def update_fornecedor_route(fornecedor_id: int, fornecedor: FornecedorUpdate, db: Session = Depends(get_db)):
    db_fornecedor = update_fornecedor(db, fornecedor_id, fornecedor)
    if db_fornecedor is None:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    return db_fornecedor

@router.delete("/fornecedores/{fornecedor_id}", response_model=Fornecedor)
def delete_fornecedor_route(fornecedor_id: int, db: Session = Depends(get_db)):
    db_fornecedor = delete_fornecedor(db, fornecedor_id)
    if db_fornecedor is None:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    return db_fornecedor
