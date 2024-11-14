from pydantic import BaseModel
from datetime import datetime

class OrdemDeCompraBase(BaseModel):
    numero: str
    chaveAcesso: str
    serie: str | None = None
    modelo: str | None = None
    dataOrdem: datetime | None = None
    dataEnvio: datetime | None = None
    observacao: str | None = None
    fornecedor_id: int
    usuario_id: int

class OrdemDeCompraCreate(OrdemDeCompraBase):
    pass

class OrdemDeCompraUpdate(OrdemDeCompraBase):
    pass

class OrdemDeCompra(OrdemDeCompraBase):
    id: int

    class Config:
        from_attributes = True
