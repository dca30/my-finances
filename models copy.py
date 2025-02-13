from sqlalchemy import Boolean, Column, ForeignKey, Integer, Float, Date, String
from database import Base

"""class Questions(Base):
    
    __tablename__ = 'questions'
    
    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String, index=True)
    
class Choices(Base):
    __tablename__ = 'choices'
    
    id = Column(Integer, primary_key=True, index=True)
    choice_text = Column(String, index=True)
    is_correct = Column(Boolean, default=False)
    question_id = Column(Integer, ForeignKey("questions.id"))"""
    
class Fondo(Base):
    __tablename__ = "fondos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True, nullable=False)
    fecha_compra = Column(Date, nullable=False)
    valor_compra = Column(Float, nullable=False)
    num_participaciones = Column(Float, nullable=False)