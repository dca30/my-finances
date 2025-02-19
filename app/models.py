from sqlalchemy import Boolean, Column, ForeignKey, Integer, Float, Date, String
from database import Base

   
class Compra(Base):
    __tablename__ = "compra"

    id = Column(Integer, primary_key=True, index=True)
    fecha_compra = Column(Date, nullable=False)
    isin = Column(String, index=True, nullable=False)
    importe = Column(Float, nullable=False)
    participaciones = Column(Float, nullable=False)
        
class Fondo(Base):
    __tablename__ = "fondo"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True, nullable=False)
    isin = Column(String, index=True, nullable=False)
    participaciones = Column(Float, nullable=False)
    rentabilidad = Column(Float, nullable=True)
    invertido = Column(Float, nullable=True)
    beneficio = Column(Float, nullable=True)