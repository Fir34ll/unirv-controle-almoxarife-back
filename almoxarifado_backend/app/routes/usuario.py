from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.usuario import Usuario, UsuarioCreate, UsuarioUpdate
from app.crud.usuario import get_usuario, get_usuarios, create_usuario, update_usuario, delete_usuario

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/usuarios/{usuario_id}", response_model=Usuario)
def read_usuario(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario = get_usuario(db, usuario_id=usuario_id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return db_usuario

@router.get("/usuarios/", response_model=list[Usuario])
def read_usuarios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_usuarios(db, skip=skip, limit=limit)

@router.post("/usuarios/", response_model=Usuario)
def create_usuario_route(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return create_usuario(db=db, usuario=usuario)

@router.put("/usuarios/{usuario_id}", response_model=Usuario)
def update_usuario_route(usuario_id: int, usuario: UsuarioUpdate, db: Session = Depends(get_db)):
    db_usuario = update_usuario(db, usuario_id, usuario)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return db_usuario

@router.delete("/usuarios/{usuario_id}", response_model=Usuario)
def delete_usuario_route(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario = delete_usuario(db, usuario_id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return db_usuario
