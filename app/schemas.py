from pydantic import BaseModel
from datetime import date
from typing import List, Optional

class FondoBase(BaseModel):
    nombre: str
    fecha_compra: date
    valor_compra: float
    num_participaciones: float

class FondoResponse(FondoBase):
    id: int

    class Config:
        from_attributes = True  # Necesario para trabajar con SQLAlchemy

class FondoUpdate(BaseModel):
    nombre: Optional[str] = None
    fecha_compra: Optional[date] = None
    valor_compra: Optional[float] = None
    num_participaciones: Optional[float] = None