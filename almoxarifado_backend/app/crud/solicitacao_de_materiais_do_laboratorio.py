from sqlalchemy.orm import Session
from app.models.solicitacao_de_materiais_do_laboratorio import SolicitacaoDeMateriaisDoLaboratorio
from app.schemas.solicitacao_de_materiais_do_laboratorio import (
    SolicitacaoDeMateriaisDoLaboratorioCreate,
    SolicitacaoDeMateriaisDoLaboratorioUpdate,
)

def get_solicitacao(db: Session, solicitacao_id: int):
    return db.query(SolicitacaoDeMateriaisDoLaboratorio).filter(SolicitacaoDeMateriaisDoLaboratorio.id == solicitacao_id).first()

def get_solicitacoes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(SolicitacaoDeMateriaisDoLaboratorio).offset(skip).limit(limit).all()

def create_solicitacao(db: Session, solicitacao: SolicitacaoDeMateriaisDoLaboratorioCreate):
    db_solicitacao = SolicitacaoDeMateriaisDoLaboratorio(**solicitacao.dict())
    db.add(db_solicitacao)
    db.commit()
    db.refresh(db_solicitacao)
    return db_solicitacao

def update_solicitacao(db: Session, solicitacao_id: int, solicitacao: SolicitacaoDeMateriaisDoLaboratorioUpdate):
    db_solicitacao = get_solicitacao(db, solicitacao_id)
    if db_solicitacao:
        for key, value in solicitacao.dict(exclude_unset=True).items():
            setattr(db_solicitacao, key, value)
        db.commit()
        db.refresh(db_solicitacao)
    return db_solicitacao

def delete_solicitacao(db: Session, solicitacao_id: int):
    db_solicitacao = get_solicitacao(db, solicitacao_id)
    if db_solicitacao:
        db.delete(db_solicitacao)
        db.commit()
    return db_solicitacao
