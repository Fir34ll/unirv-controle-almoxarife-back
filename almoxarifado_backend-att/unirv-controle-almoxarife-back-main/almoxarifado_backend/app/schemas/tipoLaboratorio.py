from pydantic import BaseModel

class TipoLaboratorioBase(BaseModel):
    descricao: str
    ativo: bool = True

class TipoLaboratorioCreate(TipoLaboratorioBase):
    pass

class TipoLaboratorioUpdate(TipoLaboratorioBase):
    pass

class TipoLaboratorio(TipoLaboratorioBase):
    id: int

    class Config:
        from_attributes = True 