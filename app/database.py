from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import DATABASE_URL

engine = create_engine(DATABASE_URL)
engine = create_engine("postgresql://myfinance:myfinance-pwd@localhost:5434/myfinance")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    """Crear las tablas en la base de datos si no existen."""
    Base.metadata.create_all(bind=engine,checkfirst=True)
    