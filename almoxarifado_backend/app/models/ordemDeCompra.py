from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class OrdemDeCompra(Base):
    __tablename__ = "ordemDeCompra"

    id = Column(Integer, primary_key=True, index=True)
    numero = Column(String(45), nullable=False)
    chaveAcesso = Column(String(200), nullable=False)
    serie = Column(String(45), nullable=True)
    modelo = Column(String(45), nullable=True)
    dataOrdem = Column(TIMESTAMP, nullable=True)
    dataEnvio = Column(TIMESTAMP, nullable=True)
    observacao = Column(String(200), nullable=True)

    fornecedor_id = Column(Integer, ForeignKey("fornecedor.id"))
    usuario_id = Column(Integer, ForeignKey("usuario.id"))

    fornecedor = relationship("Fornecedor", back_populates="ordens_de_compra")
    usuario = relationship("Usuario", back_populates="ordens_de_compra")
