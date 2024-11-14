from pydantic import BaseModel
from datetime import date
from decimal import Decimal

class LotesProdutosBase(BaseModel):
    codigoLote: str
    dataFabricacao: date
    dataValidade: date
    quantidadeRecebida: Decimal
    quantidadeAtual: Decimal
    localizacao: str | None = None
    dataRecebimento: date

class LotesProdutosCreate(LotesProdutosBase):
    ordemDeCompra_id: int
    produto_id: int

class LotesProdutosUpdate(LotesProdutosBase):
    pass

class LotesProdutos(LotesProdutosBase):
    id: int

    class Config:
        from_attributes = True 