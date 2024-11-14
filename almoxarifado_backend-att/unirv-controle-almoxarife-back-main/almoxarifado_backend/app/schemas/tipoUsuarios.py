
from pydantic import BaseModel

class TipoUsuariosBase(BaseModel):
    descricao: str
    ativo: bool = True

class TipoUsuariosCreate(TipoUsuariosBase):
    pass

class TipoUsuariosUpdate(TipoUsuariosBase):
    pass

class TipoUsuarios(TipoUsuariosBase):
    id: int

    class Config:
        from_attributes = True 
