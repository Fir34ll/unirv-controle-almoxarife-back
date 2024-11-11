from fastapi import FastAPI
from app.database import Base, engine
from app.models import usuario, tipoUsuarios, agendamento, ordemDeCompra, fornecedor, statusDaSolicitacao, solicitacao_de_materiais_do_laboratorio, departamento, campus 
from app.routes import usuario, tipoUsuarios, agendamento, ordemDeCompra, fornecedor, statusDaSolicitacao, solicitacao_de_materiais_do_laboratorio, departamento, campus

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(usuario.router, prefix="/usuarios")
app.include_router(tipoUsuarios.router, prefix="/tipousuarios")
app.include_router(agendamento.router, prefix="/agendamento")
app.include_router(ordemDeCompra.router, prefix="/ordem-de-compra")
app.include_router(fornecedor.router, prefix="/fornecedor")
app.include_router(statusDaSolicitacao.router, prefix="/status-da-solicitacao")
app.include_router(solicitacao_de_materiais_do_laboratorio.router, prefix="/solicitacoes-materiais")
app.include_router(departamento.router, prefix="/departamentos")
app.include_router(campus.router, prefix="/campus")
