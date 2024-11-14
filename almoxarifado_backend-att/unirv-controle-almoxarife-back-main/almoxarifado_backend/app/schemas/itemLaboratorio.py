from pydantic import BaseModel

class ItemLaboratorioBase(BaseModel):
    produto_id: int
    laboratorio_id: int

class ItemLaboratorioCreate(ItemLaboratorioBase):
    pass

class ItemLaboratorio(ItemLaboratorioBase):
    id: int

    class Config:
        from_attributes = True 