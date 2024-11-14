from sqlalchemy import Column, Integer, ForeignKey
from app.database import Base

class ItemLaboratorio(Base):
    __tablename__ = "itemLaboratorio"

    id = Column(Integer, primary_key=True, index=True)
    produto_id = Column(Integer, ForeignKey("produtos.id"), nullable=False)
    laboratorio_id = Column(Integer, ForeignKey("laboratorio.id"), nullable=False) 