# Bakery database

## Install and create the database

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
alembic upgrade head
```

The default database is SQLite in `bakery.db`. To use PostgreSQL instead, set
`DATABASE_URL`, for example:

```powershell
$env:DATABASE_URL = "postgresql+psycopg://user:password@localhost/bakery"
pip install psycopg[binary]
alembic upgrade head
```

## Migrations

A migration is a versioned, repeatable description of a database schema change.
It lets every developer and every deployment update the database in the same
order without manually running SQL.

After changing a model, create and review a migration:

```powershell
alembic revision --autogenerate -m "describe the change"
alembic upgrade head
```

`--autogenerate` compares the SQLAlchemy models with the current database and
creates a draft migration. Always inspect the generated file in
`migrations/versions` before applying it. To undo the latest migration locally:

```powershell
alembic downgrade -1
```

The project already contains its first migration:
`20260901_0001_initial_schema.py`.
