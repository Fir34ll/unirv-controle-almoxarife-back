from pydantic import BaseModel

class LaboratorioBase(BaseModel):
    nomeLaboratorio: str
    numeroVISA: str | None = None
    bloco: str | None = None
    tipoLaboratorio_id: int
    usuario_responsavel_id: int
    horarioInicio: str | None = None
    horarioFim: str | None = None
    ativo: bool = True

class LaboratorioCreate(LaboratorioBase):
    pass

class LaboratorioUpdate(LaboratorioBase):
    pass

class Laboratorio(LaboratorioBase):
    id: int

    class Config:
        from_attributes = True 