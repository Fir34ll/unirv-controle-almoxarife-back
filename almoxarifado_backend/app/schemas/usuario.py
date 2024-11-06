from pydantic import BaseModel, EmailStr
from datetime import datetime

class UsuarioBase(BaseModel):
    nome: str
    cpf: str
    telefone: str | None = None
    email: EmailStr
    ativo: bool = True

class UsuarioCreate(UsuarioBase):
    tipoUsuarios_id: int
    dataCriacao: datetime

class UsuarioUpdate(UsuarioBase):
    dataAtualizacao: datetime | None = None

class Usuario(UsuarioBase):
    id: int
    tipoUsuarios_id: int
    dataCriacao: datetime
    dataAtualizacao: datetime | None

    class Config:
        orm_mode = True
