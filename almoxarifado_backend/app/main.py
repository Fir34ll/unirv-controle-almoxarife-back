from fastapi import FastAPI
from app.database import Base, engine
from app.models import usuario, tipoUsuarios, agendamento, ordemDeCompra, fornecedor  
from app.routes import usuario, tipoUsuarios, agendamento, ordemDeCompra, fornecedor

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(usuario.router, prefix="/usuarios")
app.include_router(tipoUsuarios.router, prefix="/tipousuarios")
app.include_router(agendamento.router, prefix="/agendamento")
app.include_router(ordemDeCompra.router, prefix="/ordemdecompra")
app.include_router(fornecedor.router, prefix="/fornecedor")