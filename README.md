### Estrutura do Projeto
```bash
├── README.md
├── library
│   ├── __init__.py
│   ├── main.py                  # Ponto de entrada da aplicação
│   ├── config.py               # Configurações da aplicação
│   ├── models                   # Modelos de dados (SQLAlchemy)
│   │   ├── __init__.py
│   │   ├── book.py
│   │   ├── romanticist.py
│   │   └── user.py
│   ├── schemas                  # Schemas Pydantic para validação
│   │   ├── __init__.py
│   │   ├── book.py
│   │   ├── romanticist.py
│   │   └── user.py
│   ├── repositories              # Repositórios para acesso a dados
│   │   ├── __init__.py
│   │   ├── book_repository.py
│   │   ├── romanticist_repository.py
│   │   └── user_repository.py
│   ├── services                 # Lógica de negócio
│   │   ├── __init__.py
│   │   ├── book_service.py
│   │   ├── romanticist_service.py
│   │   └── user_service.py
│   ├── controllers              # Controladores (rotas)
│   │   ├── __init__.py
│   │   ├── book_controller.py
│   │   ├── romanticist_controller.py
│   │   └── user_controller.py
│   └── database.py              # Configuração do banco de dados
├── alembic                       # Diretório para migrações do Alembic
│   ├── env.py
│   ├── script.py.mako
│   ├── versions
│   └── ...
├── poetry.lock
├── pyproject.toml
└── tests                        # Testes
    ├── __init__.py
    ├── test_books.py
    ├── test_romanticists.py
    └── test_users.py
```
