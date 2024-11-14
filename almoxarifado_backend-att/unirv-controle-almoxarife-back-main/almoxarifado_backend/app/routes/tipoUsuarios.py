from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.tipoUsuarios import TipoUsuarios, TipoUsuariosCreate, TipoUsuariosUpdate
from app.crud.tipoUsuarios import get_tipo_usuario, get_tipos_usuarios, create_tipo_usuario, update_tipo_usuario, delete_tipo_usuario

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/tipos_usuarios/{tipo_usuario_id}", response_model=TipoUsuarios)
def read_tipo_usuario(tipo_usuario_id: int, db: Session = Depends(get_db)):
    db_tipo_usuario = get_tipo_usuario(db, tipo_usuario_id=tipo_usuario_id)
    if db_tipo_usuario is None:
        raise HTTPException(status_code=404, detail="Tipo de usuário não encontrado")
    return db_tipo_usuario

@router.get("/tipos_usuarios/", response_model=list[TipoUsuarios])
def read_tipos_usuarios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_tipos_usuarios(db, skip=skip, limit=limit)

@router.post("/tipos_usuarios/", response_model=TipoUsuarios)
def create_tipo_usuario_route(tipo_usuario: TipoUsuariosCreate, db: Session = Depends(get_db)):
    return create_tipo_usuario(db=db, tipo_usuario=tipo_usuario)

@router.put("/tipos_usuarios/{tipo_usuario_id}", response_model=TipoUsuarios)
def update_tipo_usuario_route(tipo_usuario_id: int, tipo_usuario: TipoUsuariosUpdate, db: Session = Depends(get_db)):
    db_tipo_usuario = update_tipo_usuario(db, tipo_usuario_id, tipo_usuario)
    if db_tipo_usuario is None:
        raise HTTPException(status_code=404, detail="Tipo de usuário não encontrado")
    return db_tipo_usuario

@router.delete("/tipos_usuarios/{tipo_usuario_id}", response_model=TipoUsuarios)
def delete_tipo_usuario_route(tipo_usuario_id: int, db: Session = Depends(get_db)):
    db_tipo_usuario = delete_tipo_usuario(db, tipo_usuario_id)
    if db_tipo_usuario is None:
        raise HTTPException(status_code=404, detail="Tipo de usuário não encontrado")
    return db_tipo_usuario
