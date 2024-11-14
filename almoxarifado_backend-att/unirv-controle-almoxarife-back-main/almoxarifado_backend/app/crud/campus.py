from sqlalchemy.orm import Session
from app.models.campus import Campus
from app.schemas.campus import CampusCreate, CampusUpdate

def get_campus(db: Session, campus_id: int):
    return db.query(Campus).filter(Campus.id == campus_id).first()

def get_campi(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Campus).offset(skip).limit(limit).all()

def create_campus(db: Session, campus: CampusCreate):
    db_campus = Campus(**campus.dict())
    db.add(db_campus)
    db.commit()
    db.refresh(db_campus)
    return db_campus

def update_campus(db: Session, campus_id: int, campus: CampusUpdate):
    db_campus = get_campus(db, campus_id)
    if db_campus:
        for key, value in campus.dict(exclude_unset=True).items():
            setattr(db_campus, key, value)
        db.commit()
        db.refresh(db_campus)
    return db_campus

def delete_campus(db: Session, campus_id: int):
    db_campus = get_campus(db, campus_id)
    if db_campus:
        db.delete(db_campus)
        db.commit()
    return db_campus
