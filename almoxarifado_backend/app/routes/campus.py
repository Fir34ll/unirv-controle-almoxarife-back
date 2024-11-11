from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.crud.campus import (
    get_campus,
    get_campi,
    create_campus,
    update_campus,
    delete_campus,
)
from app.schemas.campus import Campus, CampusCreate, CampusUpdate
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/campus/{campus_id}", response_model=Campus)
def read_campus(campus_id: int, db: Session = Depends(get_db)):
    db_campus = get_campus(db, campus_id=campus_id)
    if db_campus is None:
        raise HTTPException(status_code=404, detail="Campus não encontrado")
    return db_campus

@router.get("/campus/", response_model=List[Campus])
def read_campi(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_campi(db, skip=skip, limit=limit)

@router.post("/campus/", response_model=Campus)
def create_campus_route(campus: CampusCreate, db: Session = Depends(get_db)):
    return create_campus(db=db, campus=campus)

@router.put("/campus/{campus_id}", response_model=Campus)
def update_campus_route(campus_id: int, campus: CampusUpdate, db: Session = Depends(get_db)):
    db_campus = update_campus(db, campus_id, campus)
    if db_campus is None:
        raise HTTPException(status_code=404, detail="Campus não encontrado")
    return db_campus

@router.delete("/campus/{campus_id}", response_model=Campus)
def delete_campus_route(campus_id: int, db: Session = Depends(get_db)):
    db_campus = delete_campus(db, campus_id)
    if db_campus is None:
        raise HTTPException(status_code=404, detail="Campus não encontrado")
    return db_campus
