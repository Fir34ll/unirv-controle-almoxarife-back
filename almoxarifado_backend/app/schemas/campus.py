from pydantic import BaseModel
from typing import Optional

class CampusBase(BaseModel):
    descricao: str
    ativo: Optional[bool] = True

class CampusCreate(CampusBase):
    pass

class CampusUpdate(BaseModel):
    descricao: Optional[str] = None
    ativo: Optional[bool] = None

class Campus(CampusBase):
    id: int

    class Config:
        from_attributes = True  
