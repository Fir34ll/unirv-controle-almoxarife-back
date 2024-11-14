from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class SolicitacaoDeMateriaisDoLaboratorio(Base):
    __tablename__ = "solicitacaoDeMateriaisDoLaboratorio"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuario.id"), nullable=False)
    dataSolicitacao = Column(TIMESTAMP)
    motivoSolicitacao = Column(String(200))
    dataDecisaoSolicitacao = Column(TIMESTAMP)
    prioridade = Column(String(45))
    statusDaSolicitacao_id = Column(Integer, ForeignKey("statusDaSolicitacao.id"))
    dataAprovacao = Column(TIMESTAMP)
    dataEntrega = Column(TIMESTAMP)
    statusEntrega = Column(String(45))
    dataEntregaReal = Column(TIMESTAMP)
    responsavelPelaEntrega_id = Column(Integer, ForeignKey("usuario.id"))
    departamento_id = Column(Integer, ForeignKey("departamento.id"))
    agendamento_id = Column(Integer, ForeignKey("agendamento.id"))

    usuario = relationship("Usuario", foreign_keys=[usuario_id])
    responsavelPelaEntrega = relationship("Usuario", foreign_keys=[responsavelPelaEntrega_id])
    statusDaSolicitacao = relationship("StatusDaSolicitacao")
    departamento = relationship("Departamento")
    agendamento = relationship("Agendamento")
