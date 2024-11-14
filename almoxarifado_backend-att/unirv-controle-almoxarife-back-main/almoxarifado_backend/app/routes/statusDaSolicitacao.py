from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.statusDaSolicitacao import StatusDaSolicitacao, StatusDaSolicitacaoCreate, StatusDaSolicitacaoUpdate
from app.crud.statusDaSolicitacao import (
    get_status_da_solicitacao,
    get_status_da_solicitacoes,
    create_status_da_solicitacao,
    update_status_da_solicitacao,
    delete_status_da_solicitacao,
)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/status-da-solicitacao/{status_id}", response_model=StatusDaSolicitacao)
def read_status_da_solicitacao(status_id: int, db: Session = Depends(get_db)):
    db_status = get_status_da_solicitacao(db, status_id=status_id)
    if db_status is None:
        raise HTTPException(status_code=404, detail="Status não encontrado")
    return db_status


@router.get("/status-da-solicitacao/", response_model=list[StatusDaSolicitacao])
def read_status_da_solicitacoes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_status_da_solicitacoes(db, skip=skip, limit=limit)


@router.post("/status-da-solicitacao/", response_model=StatusDaSolicitacao)
def create_status(status: StatusDaSolicitacaoCreate, db: Session = Depends(get_db)):
    return create_status_da_solicitacao(db=db, status=status)


@router.put("/status-da-solicitacao/{status_id}", response_model=StatusDaSolicitacao)
def update_status(status_id: int, status: StatusDaSolicitacaoUpdate, db: Session = Depends(get_db)):
    db_status = update_status_da_solicitacao(
        db, status_id=status_id, status=status)
    if db_status is None:
        raise HTTPException(status_code=404, detail="Status não encontrado")
    return db_status


@router.delete("/status-da-solicitacao/{status_id}", response_model=StatusDaSolicitacao)
def delete_status(status_id: int, db: Session = Depends(get_db)):
    db_status = delete_status_da_solicitacao(db, status_id=status_id)
    if db_status is None:
        raise HTTPException(status_code=404, detail="Status não encontrado")
    return db_status
