from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Fondo(Base):
    __tablename__ = "fondos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    fecha_compra = Column(Date)
    valor_fondo = Column(Float)
    participaciones = Column(Float)
