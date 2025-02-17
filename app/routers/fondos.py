from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import date
import models, schemas
from database import SessionLocal
from schemas import FondoBase, FondoUpdate

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

@router.get("/fondos/", response_model=List[schemas.FondoResponse])
async def list_fondos(db: Session = Depends(get_db)):
    fondos = db.query(models.Fondo).all()
    return fondos

@router.delete("/fondos/{fondo_id}")
async def delete_fondo(fondo_id: int, db: Session = Depends(get_db)):
    fondo = db.query(models.Fondo).filter(models.Fondo.id == fondo_id).first()
    if not fondo:
        raise HTTPException(status_code=404, detail="Fondo not found")
    db.delete(fondo)
    db.commit()
    return {"message": "Fondo deleted successfully"}

@router.put("/fondos/{fondo_id}", response_model=schemas.FondoResponse)
async def update_fondo(fondo_id: int, fondo: FondoUpdate, db: Session = Depends(get_db)):
    db_fondo = db.query(models.Fondo).filter(models.Fondo.id == fondo_id).first()
    if not db_fondo:
        raise HTTPException(status_code=404, detail="Fondo not found")
    
    # Actualizar solo los campos que se pasen en la petición
    for key, value in fondo.model_dump(exclude_unset=True).items():
        setattr(db_fondo, key, value)

    db.commit()
    db.refresh(db_fondo)
    return db_fondo