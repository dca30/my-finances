from pydantic import BaseModel
from datetime import date

class FondoBase(BaseModel):
    nombre: str
    fecha_compra: date
    valor_compra: float
    num_participaciones: float