# 🎵 Music Albums API - FastAPI + PostgreSQL + SQLAlchemy (Async)

Projeto de estudo com FastAPI e banco de dados PostgreSQL usando SQLAlchemy assíncrono.

## 🚀 Tecnologias

- FastAPI
- PostgreSQL
- SQLAlchemy (Async ORM)
- Pydantic
- Python-dotenv

## 📦 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/FilipeMadeira13/FastAPI_CRUD_Study.git
cd FastAPI_CRUD_Study
```

2. Crie e ative o ambiente virtual:

```bash
poetry init
```

3. Instale as dependências:

```bash
poetry install --no-root
```

4. Configure o banco de dados:
   Crie um arquivo .env:

```bash
DATABASE_URL=postgresql+asyncpg://usuario:senha@localhost:5432/music_db
```

5. Crie o banco (caso não exista):

```bash
createdb music_db
```

6. Rode a criação das tabelas:

```bash
python app/create_tables.py
```

7. Inicie o servidor:

```bash
uvicorn app.main:app --reload
```

Acesse: http://localhost:8000/docs

## 📚 Endpoints

| Método | Rota         | Descrição                   |
| ------ | ------------ | --------------------------- |
| GET    | /albums      | Lista todos os álbuns       |
| GET    | /albums/{id} | Busca um álbum por ID       |
| POST   | /albums      | Cria um novo álbum          |
| PUT    | /albums/{id} | Atualiza um álbum existente |
| DELETE | /albums/{id} | Remove um álbum             |
