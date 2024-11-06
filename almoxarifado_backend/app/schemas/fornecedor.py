from pydantic import BaseModel, EmailStr
from datetime import datetime

class FornecedorBase(BaseModel):
    nomeFantasia: str
    razaoSocial: str
    cnpj: str
    endereco: str | None = None
    inscricao_estadual: str | None = None
    telefone: str | None = None
    email: EmailStr | None = None
    dataCriacao: datetime | None = None
    dataAtualizacao: datetime | None = None
    ativo: bool = True

class FornecedorCreate(FornecedorBase):
    pass

class FornecedorUpdate(FornecedorBase):
    pass

class Fornecedor(FornecedorBase):
    id: int

    class Config:
        from_attributes = True 
