from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class UnidadeDeMedida(Base):
    __tablename__ = "unidadeDeMedida"

    id = Column(Integer, primary_key=True, index=True)
    nomeUnidade = Column(String(45), nullable=False)
    ativo = Column(Boolean, default=True) 