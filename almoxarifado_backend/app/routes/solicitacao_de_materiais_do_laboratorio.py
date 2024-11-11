from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.crud.solicitacao_de_materiais_do_laboratorio import (
    get_solicitacao,
    get_solicitacoes,
    create_solicitacao,
    update_solicitacao,
    delete_solicitacao,
)
from app.schemas.solicitacao_de_materiais_do_laboratorio import (
    SolicitacaoDeMateriaisDoLaboratorio,
    SolicitacaoDeMateriaisDoLaboratorioCreate,
    SolicitacaoDeMateriaisDoLaboratorioUpdate,
)
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/solicitacoes/{solicitacao_id}", response_model=SolicitacaoDeMateriaisDoLaboratorio)
def read_solicitacao(solicitacao_id: int, db: Session = Depends(get_db)):
    db_solicitacao = get_solicitacao(db, solicitacao_id=solicitacao_id)
    if db_solicitacao is None:
        raise HTTPException(status_code=404, detail="Solicitação não encontrada")
    return db_solicitacao

@router.get("/solicitacoes/", response_model=List[SolicitacaoDeMateriaisDoLaboratorio])
def read_solicitacoes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_solicitacoes(db, skip=skip, limit=limit)

@router.post("/solicitacoes/", response_model=SolicitacaoDeMateriaisDoLaboratorio)
def create_solicitacao_route(solicitacao: SolicitacaoDeMateriaisDoLaboratorioCreate, db: Session = Depends(get_db)):
    return create_solicitacao(db=db, solicitacao=solicitacao)

@router.put("/solicitacoes/{solicitacao_id}", response_model=SolicitacaoDeMateriaisDoLaboratorio)
def update_solicitacao_route(solicitacao_id: int, solicitacao: SolicitacaoDeMateriaisDoLaboratorioUpdate, db: Session = Depends(get_db)):
    db_solicitacao = update_solicitacao(db, solicitacao_id, solicitacao)
    if db_solicitacao is None:
        raise HTTPException(status_code=404, detail="Solicitação não encontrada")
    return db_solicitacao

@router.delete("/solicitacoes/{solicitacao_id}", response_model=SolicitacaoDeMateriaisDoLaboratorio)
def delete_solicitacao_route(solicitacao_id: int, db: Session = Depends(get_db)):
    db_solicitacao = delete_solicitacao(db, solicitacao_id)
    if db_solicitacao is None:
        raise HTTPException(status_code=404, detail="Solicitação não encontrada")
    return db_solicitacao
