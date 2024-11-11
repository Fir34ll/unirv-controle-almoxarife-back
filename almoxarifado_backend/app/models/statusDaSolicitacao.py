from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class StatusDaSolicitacao(Base):
    __tablename__ = "statusDaSolicitacao"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String(45), nullable=False)
    finalizado = Column(Boolean, default=False)
    ativo = Column(Boolean, default=True)
