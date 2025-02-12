from sqlalchemy import Column, Integer, String, Float, Date
from app.database import Base

class Fondo(Base):
    __tablename__ = "fondos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True, nullable=False)
    fecha_compra = Column(Date, nullable=False)
    valor_compra = Column(Float, nullable=False)
    num_participaciones = Column(Float, nullable=False)
