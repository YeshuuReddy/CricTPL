"""
database.py
------------

This file handles:
1. Database connection setup
2. Dependency injection for DB sessions
3. Database initialization (creating tables)

IT Company Best Practices:
- Type hints for clarity
- Docstrings for every function
- Lazy imports for models
- Scalable for multiple models
"""

from typing import Generator
from sqlmodel import SQLModel, Session, create_engine
from app.core.config import settings

# -------------------------
# DATABASE ENGINE
# -------------------------
# SQLAlchemy engine configuration
# - echo=False : disables SQL logging in production (enable in dev)
# - future=True : SQLAlchemy 2.x style queries
engine = create_engine(
    settings.DATABASE_URL,
    echo=False,  # Set True in dev for debugging
    future=True
)


# -------------------------
# DEPENDENCY INJECTION
# -------------------------
def get_session() -> Generator[Session, None, None]:
    """
    Provides a database session to FastAPI routes.
    Use with FastAPI Depends().

    Example:
        @app.get("/players")
        def get_players(session: Session = Depends(get_session)):
            ...
    """
    with Session(engine) as session:
        yield session


# -------------------------
# DATABASE INITIALIZATION
# -------------------------
def init_db() -> None:
    """
    Initializes the database by creating all tables defined in SQLModel models.
    Call this during application startup.

    IT Company Standard:
    - Import all models here to avoid circular imports
    - Supports scalability for future tables
    """
    # Import all your models here
    # from app.db.models.teams import Team
    # from app.db.models.matches import Match

    # Creates all tables that do not exist
    SQLModel.metadata.create_all(bind=engine)
