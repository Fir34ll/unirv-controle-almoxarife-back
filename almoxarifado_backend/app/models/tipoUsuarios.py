
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class TipoUsuarios(Base):
    __tablename__ = "tipoUsuarios"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String(45), nullable=False)
    ativo = Column(Boolean, default=True)

    usuarios = relationship("Usuario", back_populates="tipo_usuario")
