from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class TipoLaboratorio(Base):
    __tablename__ = "tipoLaboratorio"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String(45), nullable=False)
    ativo = Column(Boolean, default=True) 