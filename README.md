# FastAPI Pizzeria API

Backend de um sistema de delivery de pizzaria desenvolvido com **FastAPI**, utilizando **SQLAlchemy** como ORM e **Alembic** para versionamento e migração de banco de dados.

Este projeto simula uma API real de produção com arquitetura modular, separação de responsabilidades e versionamento estruturado de banco de dados.

## Tecnologias Utilizadas

-   **FastAPI** - Framework moderno para construção de APIs
-   **SQLAlchemy** - ORM para modelagem e manipulação do banco
-   **Alembic** - Controle de migrações do banco de dados
-   **SQLite** - Banco de dados local para desenvolvimento
-   **Uvicorn** - Servidor ASGI

## Estrutura do Projeto

```
fastapi-pizzeria-api/
│
├── alembic/                # Configurações e versões de migração
├── models.py               # Modelos do banco de dados
├── auth_routes.py          # Rotas de autenticação
├── order_routes.py         # Rotas de pedidos
├── main.py                 # Inicialização da aplicação
├── alembic.ini             # Configuração do Alembic
├── requirements.txt        # Dependências do projeto
└── README.md
```

## Arquitetura

A aplicação segue uma arquitetura modular baseada em:

-   Separação de rotas por domínio (Auth / Orders)
-   ORM com modelos declarativos
-   Versionamento de banco via migrações
-   Estrutura preparada para escalar para PostgreSQL ou outro banco SQL

## Modelagem do Banco de Dados

O sistema possui três entidades principais:

### Usuário
-   id (PK)
-   nome
-   email
-   senha
-   ativo
-   admin

### Pedido
-   id (PK)
-   status
-   usuario_id (FK → usuarios.id)
-   preco

### Item do Pedido
-   id (PK)
-   quantidade
-   sabor
-   tamanho
-   preco_unitario
-   pedido_id (FK → pedidos.id)

Relacionamentos:
-   Um usuário pode ter vários pedidos
-   Um pedido pode ter vários itens

## Como Rodar o Projeto

### 1. Criar ambiente virtual

```bash
python -m venv venv
```

Ativar:

**Windows**

```bash
venc\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Rodar migrações do banco

```bash
alembic upgrade head
```

Isso criará o banco `banco.db` com todas as tabelas.

### 4. Executar servidor

```bash
uvicorn main:app --reload
```

A API estará disponível em:

`http://127.0.0.1:8000`

Documentação automática:

`http://127.0.0.1:8000/docs`

## Criando Nova Migração

Sempre que alterar algum modelo:

```bash
alembic revision --autogenerate -m "descrição_da_mudança"
alembic upgrade head
```

## Endpoints Atuais

### Auth

*   `GET /auth/`

### Pedidos

*   `GET /orders/`

## Status do Projeto

*   [x] Estrutura inicial da API
*   [x] Organização modular de rotas
*   [x] Modelagem completa do banco
*   [x] Integração com SQLAlchemy
*   [x] Configuração de Alembic
*   [x] Migração inicial aplicada
*   [ ] Implementação de CRUD completo
*   [ ] Autenticação com JWT
*   [ ] Deploy em ambiente cloud

## Próximos Passos

*   Implementar criação real de usuários
*   CRUD completo de pedidos
*   Validações com Pydantic
*   Autenticação com JWT
*   Deploy com PostgreSQL

## Objetivo do Projeto

Este projeto tem como objetivo:

*   Demonstrar domínio de backend com FastAPI
*   Aplicar modelagem relacional com SQLAlchemy
*   Trabalhar versionamento de banco com Alembic
*   Simular arquitetura próxima a ambiente de produção

## Autor

Matheus Sousa Martins
Projeto desenvolvido para estudo e evolução em Backend Python.
