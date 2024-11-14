from sqlalchemy.orm import Session
from app.models.tipoUsuarios import TipoUsuarios
from app.schemas.tipoUsuarios import TipoUsuariosCreate, TipoUsuariosUpdate

def get_tipo_usuario(db: Session, tipo_usuario_id: int):
    return db.query(TipoUsuarios).filter(TipoUsuarios.id == tipo_usuario_id).first()

def get_tipos_usuarios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(TipoUsuarios).offset(skip).limit(limit).all()

def create_tipo_usuario(db: Session, tipo_usuario: TipoUsuariosCreate):
    db_tipo_usuario = TipoUsuarios(**tipo_usuario.dict())
    db.add(db_tipo_usuario)
    db.commit()
    db.refresh(db_tipo_usuario)
    return db_tipo_usuario

def update_tipo_usuario(db: Session, tipo_usuario_id: int, tipo_usuario: TipoUsuariosUpdate):
    db_tipo_usuario = get_tipo_usuario(db, tipo_usuario_id)
    if db_tipo_usuario:
        for key, value in tipo_usuario.dict(exclude_unset=True).items():
            setattr(db_tipo_usuario, key, value)
        db.commit()
        db.refresh(db_tipo_usuario)
        return db_tipo_usuario
    return None

def delete_tipo_usuario(db: Session, tipo_usuario_id: int):
    db_tipo_usuario = get_tipo_usuario(db, tipo_usuario_id)
    if db_tipo_usuario:
        db.delete(db_tipo_usuario)
        db.commit()
        return db_tipo_usuario
    return None
