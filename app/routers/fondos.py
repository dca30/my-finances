from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import date
import models
from database import SessionLocal
from schemas import FondoBase

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.get("/fondos/{fondo_id}")
async def read_fondo(fondo_id: int, db: Session = Depends(get_db)):
    result = db.query(models.Fondo).filter(models.Fondo.id == fondo_id).first()
    if not result:
        raise HTTPException(status_code=404, detail='Fondo not found')
    return result

@router.post("/fondos/")
async def create_fondo(fondo: FondoBase, db: Session = Depends(get_db)):
    db_fondo = models.Fondo(
        nombre=fondo.nombre,
        fecha_compra=fondo.fecha_compra,
        valor_compra=fondo.valor_compra,
        num_participaciones=fondo.num_participaciones
    )
    db.add(db_fondo)
    db.commit()
    db.refresh(db_fondo)
    return db_fondo

@router.get("/fondos/", response_model=List[models.Fondo])
async def list_fondos(db: Session = Depends(get_db)):
    fondos = db.query(models.Fondo).all()
    return fondos