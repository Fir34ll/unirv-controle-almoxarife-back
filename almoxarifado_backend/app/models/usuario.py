from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from app.database import Base

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True)
    tipoUsuarios_id = Column(Integer, ForeignKey("tipoUsuarios.id"))
    nome = Column(String(45), nullable=False)
    cpf = Column(String(45), unique=True, nullable=False)
    telefone = Column(String(45), nullable=True)
    email = Column(String(45), unique=True, nullable=False)
    dataCriacao = Column(TIMESTAMP, nullable=False)
    dataAtualizacao = Column(TIMESTAMP, nullable=True)
    ativo = Column(Boolean, default=True)

    tipo_usuario = relationship("TipoUsuarios", back_populates="usuarios")

    ordens_de_compra = relationship("OrdemDeCompra", back_populates="usuario")
