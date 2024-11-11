from pydantic import BaseModel
from typing import Optional


class StatusDaSolicitacaoBase(BaseModel):
    descricao: str
    finalizado: Optional[bool] = False
    ativo: Optional[bool] = True


class StatusDaSolicitacaoCreate(StatusDaSolicitacaoBase):
    pass


class StatusDaSolicitacaoUpdate(BaseModel):
    descricao: Optional[str] = None
    finalizado: Optional[bool] = None
    ativo: Optional[bool] = None


class StatusDaSolicitacao(StatusDaSolicitacaoBase):
    id: int

    class Config:
        from_attributes = True
