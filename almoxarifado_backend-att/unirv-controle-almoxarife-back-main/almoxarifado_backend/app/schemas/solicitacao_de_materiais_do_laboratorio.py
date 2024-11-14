from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SolicitacaoDeMateriaisDoLaboratorioBase(BaseModel):
    usuario_id: int
    dataSolicitacao: Optional[datetime] = None
    motivoSolicitacao: Optional[str] = None
    dataDecisaoSolicitacao: Optional[datetime] = None
    prioridade: Optional[str] = None
    statusDaSolicitacao_id: Optional[int] = None
    dataAprovacao: Optional[datetime] = None
    dataEntrega: Optional[datetime] = None
    statusEntrega: Optional[str] = None
    dataEntregaReal: Optional[datetime] = None
    responsavelPelaEntrega_id: Optional[int] = None
    departamento_id: Optional[int] = None
    agendamento_id: Optional[int] = None

class SolicitacaoDeMateriaisDoLaboratorioCreate(SolicitacaoDeMateriaisDoLaboratorioBase):
    pass

class SolicitacaoDeMateriaisDoLaboratorioUpdate(BaseModel):
    usuario_id: Optional[int] = None
    dataSolicitacao: Optional[datetime] = None
    motivoSolicitacao: Optional[str] = None
    dataDecisaoSolicitacao: Optional[datetime] = None
    prioridade: Optional[str] = None
    statusDaSolicitacao_id: Optional[int] = None
    dataAprovacao: Optional[datetime] = None
    dataEntrega: Optional[datetime] = None
    statusEntrega: Optional[str] = None
    dataEntregaReal: Optional[datetime] = None
    responsavelPelaEntrega_id: Optional[int] = None
    departamento_id: Optional[int] = None
    agendamento_id: Optional[int] = None

class SolicitacaoDeMateriaisDoLaboratorio(SolicitacaoDeMateriaisDoLaboratorioBase):
    id: int

    class Config:
        from_attributes = True
