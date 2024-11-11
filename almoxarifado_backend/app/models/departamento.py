from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Departamento(Base):
    __tablename__ = "departamento"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String(45), nullable=False)
    ativo = Column(Boolean, default=True)
    campus_id = Column(Integer, ForeignKey("campus.id"))

    campus = relationship("Campus", back_populates="departamentos")
