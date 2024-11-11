from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class Campus(Base):
    __tablename__ = "campus"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String(45), nullable=False)
    ativo = Column(Boolean, default=True)

    departamentos = relationship("Departamento", back_populates="campus")
