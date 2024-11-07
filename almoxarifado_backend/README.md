Projeto de Controle de Almoxarifado - Backend
Este projeto é o backend de um sistema de controle de almoxarifado, desenvolvido em Python com o framework FastAPI.

--------------------------------------------------------------------------

- Ferramentas atuais utilizadas:
Python 3.11 - Linguagem de programação principal.
FastAPI - Framework web para criação de APIs rápidas e eficientes.
SQLAlchemy - ORM (Object-Relational Mapping) para manipulação do banco de dados relacional.
SQLite - Banco de dados usado temporariamente para desenvolvimento local, já que não tem acesso ao PostgreSQL ainda.
Pydantic - Biblioteca para validação de dados.
Uvicorn - Servidor ASGI para rodar o aplicativo FastAPI.

--------------------------------------------------------------------------

- O arquivo requirements.txt contém as dependências atuais do projeto:
fastapi
uvicorn
sqlalchemy
pydantic[email]
pydantic-settings

Para baixar as dependências use o comando: pip install -r requirements.txt 

--------------------------------------------------------------------------

- Estrutura de Diretórios
A estrutura de diretórios do projeto é organizada da seguinte forma:

almoxarifado_backend/
├── app/
│   ├── main.py              # Ponto de entrada do FastAPI
│   ├── config.py            # Configurações do projeto
│   ├── database.py          # Configuração de conexão com o banco de dados
|   ├── test.db              # Quando o comando 'uvicorn app.main:app --reload', for rodado, o banco local será criado
│   ├── models/              # Modelos SQLAlchemy
│   │   ├── usuario.py       # Exemplo de códigos
│   │   ├── tipoUsuarios.py
│   │   └── agendamento.py
│   ├── schemas/             # Schemas Pydantic
│   │   ├── usuario.py       # Exemplo de códigos
│   │   ├── tipoUsuarios.py
│   │   └── agendamento.py
│   ├── crud/                # Funções de CRUD
│   │   ├── usuario.py       # Exemplo de códigos
│   │   ├── tipoUsuarios.py
│   │   └── agendamento.py
│   └── routes/              # Rotas de API
│       ├── usuario.py       # Exemplo de códigos
│       ├── tipoUsuarios.py
│       └── agendamento.py

Pastas:
- crud
- models
- routes
- schemas

--------------------------------------------------------------------------

- A URL do banco de dados é configurada no arquivo app/config.py. Para o SQLite, a configuração atual usa:
DATABASE_URL = "sqlite:///./test.db"

O SQLite criará o arquivo test.db na primeira execução, e será possível desenvolver e testar o backend como se estivesse usando um 
banco de dados completo.

- Para usar o banco de dados em produção, será preciso alterar o DATABASE_URL para a URL do banco de dados, como por exemplo:
DATABASE_URL = "postgresql://usuario:senha@localhost:5432/nome_do_banco"

--------------------------------------------------------------------------

- Rodando o Projeto:
Após instalar as dependências e configurar o banco de dados, rode o seguinte comando:

uvicorn app.main:app --reload

Esse comando inicia o servidor em modo de desenvolvimento com recarga automática. O servidor estará acessível em http://127.0.0.1:8000

- Acesse a documentação interativa:
FastAPI gera automaticamente uma documentação interativa da API, acessível nos seguintes endpoints:

Swagger UI: http://127.0.0.1:8000/docs
Redoc: http://127.0.0.1:8000/redoc

É possível testar todas as rotas diretamente nesses endpoints.

--------------------------------------------------------------------------