from pydantic import BaseModel
from typing import Optional

class DepartamentoBase(BaseModel):
    descricao: str
    ativo: Optional[bool] = True
    campus_id: Optional[int] = None

class DepartamentoCreate(DepartamentoBase):
    pass

class DepartamentoUpdate(BaseModel):
    descricao: Optional[str] = None
    ativo: Optional[bool] = None
    campus_id: Optional[int] = None

class Departamento(DepartamentoBase):
    id: int

    class Config:
        from_attributes = True
