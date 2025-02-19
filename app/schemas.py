from pydantic import BaseModel
from datetime import date
from typing import List, Optional

class FondoBase(BaseModel):
    nombre: str
    isin: str
    participaciones: float
    rentabilidad: float
    invertido: float
    beneficio: float

class FondoResponse(FondoBase):
    id: int

    class Config:
        from_attributes = True

class FondoUpdate(BaseModel):
    nombre: Optional[str] = None
    isin: Optional[str] = None
    participaciones: Optional[float] = None
    rentabilidad: Optional[float] = None
    invertido: Optional[float] = None
    beneficio: Optional[float] = None