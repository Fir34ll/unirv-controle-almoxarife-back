from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.agendamento import Agendamento, AgendamentoCreate, AgendamentoUpdate
from app.crud.agendamento import get_agendamento, get_agendamentos, create_agendamento, update_agendamento, delete_agendamento

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/agendamentos/{agendamento_id}", response_model=Agendamento)
def read_agendamento(agendamento_id: int, db: Session = Depends(get_db)):
    db_agendamento = get_agendamento(db, agendamento_id=agendamento_id)
    if db_agendamento is None:
        raise HTTPException(status_code=404, detail="Agendamento não encontrado")
    return db_agendamento

@router.get("/agendamentos/", response_model=list[Agendamento])
def read_agendamentos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_agendamentos(db, skip=skip, limit=limit)

@router.post("/agendamentos/", response_model=Agendamento)
def create_agendamento_route(agendamento: AgendamentoCreate, db: Session = Depends(get_db)):
    return create_agendamento(db=db, agendamento=agendamento)

@router.put("/agendamentos/{agendamento_id}", response_model=Agendamento)
def update_agendamento_route(agendamento_id: int, agendamento: AgendamentoUpdate, db: Session = Depends(get_db)):
    db_agendamento = update_agendamento(db, agendamento_id, agendamento)
    if db_agendamento is None:
        raise HTTPException(status_code=404, detail="Agendamento não encontrado")
    return db_agendamento

@router.delete("/agendamentos/{agendamento_id}", response_model=Agendamento)
def delete_agendamento_route(agendamento_id: int, db: Session = Depends(get_db)):
    db_agendamento = delete_agendamento(db, agendamento_id)
    if db_agendamento is None:
        raise HTTPException(status_code=404, detail="Agendamento não encontrado")
    return db_agendamento
