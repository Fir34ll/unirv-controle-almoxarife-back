from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP
from sqlalchemy.orm import relationship
from app.database import Base

class Fornecedor(Base):
    __tablename__ = "fornecedor"

    id = Column(Integer, primary_key=True, index=True)
    nomeFantasia = Column(String(45), nullable=False)
    razaoSocial = Column(String(45), nullable=False)
    cnpj = Column(String(45), unique=True, nullable=False)
    endereco = Column(String(45), nullable=True)
    inscricao_estadual = Column(String(45), nullable=True)
    telefone = Column(String(45), nullable=True)
    email = Column(String(45), nullable=True)
    dataCriacao = Column(TIMESTAMP, nullable=True)
    dataAtualizacao = Column(TIMESTAMP, nullable=True)
    ativo = Column(Boolean, default=True)

    ordens_de_compra = relationship("OrdemDeCompra", back_populates="fornecedor")