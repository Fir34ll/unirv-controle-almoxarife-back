from sqlalchemy import Column, Integer, String
from app.database import Base

class Agendamento(Base):
    __tablename__ = "agendamento"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(45), nullable=False)
    termino = Column(String(45), nullable=False)
    dataInicio = Column(String(45), nullable=False)
