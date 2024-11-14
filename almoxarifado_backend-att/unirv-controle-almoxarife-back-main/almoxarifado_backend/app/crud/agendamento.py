from sqlalchemy.orm import Session
from app.models.agendamento import Agendamento
from app.schemas.agendamento import AgendamentoCreate, AgendamentoUpdate

def get_agendamento(db: Session, agendamento_id: int):
    return db.query(Agendamento).filter(Agendamento.id == agendamento_id).first()

def get_agendamentos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Agendamento).offset(skip).limit(limit).all()

def create_agendamento(db: Session, agendamento: AgendamentoCreate):
    db_agendamento = Agendamento(**agendamento.dict())
    db.add(db_agendamento)
    db.commit()
    db.refresh(db_agendamento)
    return db_agendamento

def update_agendamento(db: Session, agendamento_id: int, agendamento: AgendamentoUpdate):
    db_agendamento = get_agendamento(db, agendamento_id)
    if db_agendamento:
        for key, value in agendamento.dict(exclude_unset=True).items():
            setattr(db_agendamento, key, value)
        db.commit()
        db.refresh(db_agendamento)
        return db_agendamento
    return None

def delete_agendamento(db: Session, agendamento_id: int):
    db_agendamento = get_agendamento(db, agendamento_id)
    if db_agendamento:
        db.delete(db_agendamento)
        db.commit()
        return db_agendamento
    return None
