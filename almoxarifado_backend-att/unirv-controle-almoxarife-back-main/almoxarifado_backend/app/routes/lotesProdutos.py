from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.lotesProdutos import LotesProdutos, LotesProdutosCreate, LotesProdutosUpdate
from app.crud.lotesProdutos import get_lote_produto, get_lotes_produtos, create_lote_produto, update_lote_produto, delete_lote_produto

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/lotes-produtos/{lote_id}", response_model=LotesProdutos)
def read_lote_produto(lote_id: int, db: Session = Depends(get_db)):
    db_lote = get_lote_produto(db, lote_id=lote_id)
    if db_lote is None:
        raise HTTPException(status_code=404, detail="Lote de Produto não encontrado")
    return db_lote

@router.get("/lotes-produtos/", response_model=list[LotesProdutos])
def read_lotes_produtos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_lotes_produtos(db, skip=skip, limit=limit)

@router.post("/lotes-produtos/", response_model=LotesProdutos)
def create_lote_produto_route(lote: LotesProdutosCreate, db: Session = Depends(get_db)):
    return create_lote_produto(db=db, lote=lote)

@router.put("/lotes-produtos/{lote_id}", response_model=LotesProdutos)
def update_lote_produto_route(lote_id: int, lote: LotesProdutosUpdate, db: Session = Depends(get_db)):
    db_lote = update_lote_produto(db, lote_id, lote)
    if db_lote is None:
        raise HTTPException(status_code=404, detail="Lote de Produto não encontrado")
    return db_lote

@router.delete("/lotes-produtos/{lote_id}", response_model=LotesProdutos)
def delete_lote_produto_route(lote_id: int, db: Session = Depends(get_db)):
    db_lote = delete_lote_produto(db, lote_id)
    if db_lote is None:
        raise HTTPException(status_code=404, detail="Lote de Produto não encontrado")
    return db_lote 