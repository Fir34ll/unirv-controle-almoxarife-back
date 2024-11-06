from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.ordemDeCompra import OrdemDeCompra, OrdemDeCompraCreate, OrdemDeCompraUpdate
from app.crud.ordemDeCompra import get_ordem_de_compra, get_ordens_de_compra, create_ordem_de_compra, update_ordem_de_compra, delete_ordem_de_compra

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/ordens_de_compra/{ordem_id}", response_model=OrdemDeCompra)
def read_ordem_de_compra(ordem_id: int, db: Session = Depends(get_db)):
    db_ordem = get_ordem_de_compra(db, ordem_id=ordem_id)
    if db_ordem is None:
        raise HTTPException(status_code=404, detail="Ordem de compra não encontrada")
    return db_ordem

@router.get("/ordens_de_compra/", response_model=list[OrdemDeCompra])
def read_ordens_de_compra(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_ordens_de_compra(db, skip=skip, limit=limit)

@router.post("/ordens_de_compra/", response_model=OrdemDeCompra)
def create_ordem_de_compra_route(ordem: OrdemDeCompraCreate, db: Session = Depends(get_db)):
    return create_ordem_de_compra(db=db, ordem=ordem)

@router.put("/ordens_de_compra/{ordem_id}", response_model=OrdemDeCompra)
def update_ordem_de_compra_route(ordem_id: int, ordem: OrdemDeCompraUpdate, db: Session = Depends(get_db)):
    db_ordem = update_ordem_de_compra(db, ordem_id, ordem)
    if db_ordem is None:
        raise HTTPException(status_code=404, detail="Ordem de compra não encontrada")
    return db_ordem

@router.delete("/ordens_de_compra/{ordem_id}", response_model=OrdemDeCompra)
def delete_ordem_de_compra_route(ordem_id: int, db: Session = Depends(get_db)):
    db_ordem = delete_ordem_de_compra(db, ordem_id)
    if db_ordem is None:
        raise HTTPException(status_code=404, detail="Ordem de compra não encontrada")
    return db_ordem
