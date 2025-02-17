from sqlalchemy import Boolean, Column, ForeignKey, Integer, Float, Date, String
from database import Base

   
class Fondo(Base):
    __tablename__ = "fondos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True, nullable=False)
    fecha_compra = Column(Date, nullable=False)
    valor_compra = Column(Float, nullable=False)
    num_participaciones = Column(Float, nullable=False)