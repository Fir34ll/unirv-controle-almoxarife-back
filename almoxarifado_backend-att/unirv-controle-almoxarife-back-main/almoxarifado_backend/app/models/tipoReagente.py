from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class TipoReagente(Base):
    __tablename__ = "tipoReagente"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(45), nullable=False)
    ativo = Column(Boolean, default=True) 