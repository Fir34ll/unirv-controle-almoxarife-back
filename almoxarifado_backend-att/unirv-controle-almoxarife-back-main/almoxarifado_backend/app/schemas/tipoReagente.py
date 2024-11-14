from pydantic import BaseModel

class TipoReagenteBase(BaseModel):
    nome: str
    ativo: bool = True

class TipoReagenteCreate(TipoReagenteBase):
    pass

class TipoReagenteUpdate(TipoReagenteBase):
    pass

class TipoReagente(TipoReagenteBase):
    id: int

    class Config:
        from_attributes = True 