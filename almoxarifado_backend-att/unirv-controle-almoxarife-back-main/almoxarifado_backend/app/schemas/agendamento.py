
from pydantic import BaseModel

class AgendamentoBase(BaseModel):
    titulo: str
    termino: str
    dataInicio: str

class AgendamentoCreate(AgendamentoBase):
    pass

class AgendamentoUpdate(AgendamentoBase):
    pass

class Agendamento(AgendamentoBase):
    id: int

    class Config:
        from_attributes = True 
