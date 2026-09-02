"""SQLAlchemy 2.0 configuration and database-session helpers."""

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///bakery.db")


class Base(DeclarativeBase):
    pass


engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine, class_=Session, expire_on_commit=False)


def create_tables() -> None:
    """Create all tables locally. Use Alembic migrations in shared/production databases."""
    import src.models  # noqa: F401 - registers mapped classes with Base.metadata

    Base.metadata.create_all(engine)
