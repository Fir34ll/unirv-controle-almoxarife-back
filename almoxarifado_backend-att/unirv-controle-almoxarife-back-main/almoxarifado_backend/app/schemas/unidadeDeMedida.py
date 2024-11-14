from pydantic import BaseModel

class UnidadeDeMedidaBase(BaseModel):
    nomeUnidade: str
    ativo: bool = True

class UnidadeDeMedidaCreate(UnidadeDeMedidaBase):
    pass

class UnidadeDeMedidaUpdate(UnidadeDeMedidaBase):
    pass

class UnidadeDeMedida(UnidadeDeMedidaBase):
    id: int

    class Config:
        from_attributes = True 