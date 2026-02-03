# 🚀 FastAPI Template

A clean and scalable **FastAPI template** designed to build modern APIs with support for **PostgreSQL** and **Oracle** databases.

This template is ideal for:
- New API projects
- Microservices
- Enterprise backends
- Production-ready FastAPI applications

---

## ✨ Features

- ⚡ FastAPI
- 🧱 Modular and scalable architecture
- 🐘 PostgreSQL (SQLAlchemy + psycopg)
- 🟠 Oracle (SQLAlchemy + oracledb)
- 🔐 Environment-based configuration
- 📦 Virtual environment friendly
- 🧪 Ready to grow (services, utils, migrations)

---

## 📁 Project Structure

```text
FASTAPI-TEMPLATE/
│
├── api/                # API routes / endpoints
│   └── __init__.py
├── core/               # Global configuration
│   └── config.py
├── db/                 # Database connections
│   ├── oracle.py
│   └── postgresql.py
├── models/             # SQLAlchemy models
│   └── entityModel.py
├── schemas/            # Pydantic schemas
│   ├── DatabaseResponse.py
│   └── responseModel.py
├── services/           # Business logic
│   └── __init__.py
├── utils/              # Utility helpers
├── vtemplate/          # Project-specific templates
├── .env                # Environment variables (ignored)
├── .gitignore
├── main.py             # Application entry point
└── requirements.txt
```

## ⚙️ Requirements

- Python 3.9+
- Git
- PostgreSQL and/or Oracle (optional, depending on your use case)
- Virtual environment tool (venv, virtualenv)

## 📦 Installation
```bash
git clone https://github.com/Vlonetatii3/fastapi-template.git
cd fastapi-template
python -m venv .venv

```

### Activate the virtual environment

Windows
```bash
.venv\Scripts\activate
```

Linux / macOS
```bash
source .venv/bin/activate
```

Install dependencies
```bash
pip install -r requirements.txt
```


## 🔐 Environment Configuration

Create a .env file in the project root:

### PostgreSQL
POSTGRES_USER=postgres
POSTGRES_PASSWORD=secret
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=fastapi_db

### Oracle
ORACLE_USER=app_user
ORACLE_PASSWORD=secret
ORACLE_HOST=localhost
ORACLE_PORT=1521
ORACLE_SERVICE=ORCLPDB1


#### ✅ Tip: you can also add a .env.example file (committed) and keep .env private (ignored).


## 🧠 Database Usage

This template includes separate DB modules for PostgreSQL and Oracle. Use FastAPI dependencies to inject a session where needed.

PostgreSQL Example
```bash
from fastapi import Depends
from sqlalchemy.orm import Session
from db.postgresql import get_postgres_db

def example(db: Session = Depends(get_postgres_db)):
    ...
```

Oracle Example
```bash
from fastapi import Depends
from sqlalchemy.orm import Session
from db.oracle import get_oracle_db

def example(db: Session = Depends(get_oracle_db)):
    ...
```

## ✅ What’s Included (Best Practices)

- Separation of concerns (API / services / models / schemas)

- Environment-based settings (no hardcoded secrets)

- Dependency-based DB sessions (clean session lifecycle)

- Ready-to-extend structure for production projects

## 🗺️ Roadmap

- Alembic migrations support

- Docker / docker-compose setup

- Async database support (asyncpg / Oracle async)

- Auth module (JWT / OAuth2)

- Tests setup (pytest)