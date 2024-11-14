from sqlalchemy import Column, Integer, String, Time, Boolean, ForeignKey
from app.database import Base

class Laboratorio(Base):
    __tablename__ = "laboratorio"

    id = Column(Integer, primary_key=True, index=True)
    nomeLaboratorio = Column(String(50), nullable=False)
    numeroVISA = Column(String(45), nullable=True)
    bloco = Column(String(45), nullable=True)
    tipoLaboratorio_id = Column(Integer, ForeignKey("tipoLaboratorio.id"), nullable=False)
    usuario_responsavel_id = Column(Integer, ForeignKey("usuario.id"), nullable=False)
    horarioInicio = Column(Time, nullable=True)
    horarioFim = Column(Time, nullable=True)
    ativo = Column(Boolean, default=True) 