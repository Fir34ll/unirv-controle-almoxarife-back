from sqlalchemy import Column, Integer, String, Date, DECIMAL, ForeignKey
from app.database import Base

class LotesProdutos(Base):
    __tablename__ = "lotesProdutos"

    id = Column(Integer, primary_key=True, index=True)
    codigoLote = Column(String(50), nullable=False)
    dataFabricacao = Column(Date, nullable=False)
    dataValidade = Column(Date, nullable=False)
    quantidadeRecebida = Column(DECIMAL(10, 3), nullable=False)
    quantidadeAtual = Column(DECIMAL(10, 3), nullable=False)
    localizacao = Column(String(200), nullable=True)
    dataRecebimento = Column(Date, nullable=False)
    ordemDeCompra_id = Column(Integer, ForeignKey("ordemDeCompra.id"), nullable=False)
    produto_id = Column(Integer, ForeignKey("produtos.id"), nullable=False) 