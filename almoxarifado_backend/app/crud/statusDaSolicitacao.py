from sqlalchemy.orm import Session
from app.models.statusDaSolicitacao import StatusDaSolicitacao
from app.schemas.statusDaSolicitacao import StatusDaSolicitacaoCreate, StatusDaSolicitacaoUpdate

def get_status_da_solicitacao(db: Session, status_id: int):
    return db.query(StatusDaSolicitacao).filter(StatusDaSolicitacao.id == status_id).first()

def get_status_da_solicitacoes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(StatusDaSolicitacao).offset(skip).limit(limit).all()

def create_status_da_solicitacao(db: Session, status: StatusDaSolicitacaoCreate):
    db_status = StatusDaSolicitacao(**status.dict())
    db.add(db_status)
    db.commit()
    db.refresh(db_status)
    return db_status

def update_status_da_solicitacao(db: Session, status_id: int, status: StatusDaSolicitacaoUpdate):
    db_status = get_status_da_solicitacao(db, status_id)
    if db_status:
        for key, value in status.dict(exclude_unset=True).items():
            setattr(db_status, key, value)
        db.commit()
        db.refresh(db_status)
        return db_status
    return None

def delete_status_da_solicitacao(db: Session, status_id: int):
    db_status = get_status_da_solicitacao(db, status_id)
    if db_status:
        db.delete(db_status)
        db.commit()
        return db_status
    return None
