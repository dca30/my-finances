from datetime import date
import pandas as pd
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session
import models
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint para subir archivos CSV
EXPECTED_COLUMNS = {"nombre", "fecha_compra", "valor_compra", "num_participaciones"}

@router.post("/upload_csv/")
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        # Leer CSV con Pandas
        df = pd.read_csv(file.file)

        # Validar que tiene las columnas correctas
        if not EXPECTED_COLUMNS.issubset(df.columns):
            raise HTTPException(status_code=400, detail=f"El CSV debe contener las columnas: {EXPECTED_COLUMNS}")

        # Convertir fecha de string a formato datetime
        try:
            df["fecha_compra"] = pd.to_datetime(df["fecha_compra"], format="%Y-%m-%d")
        except ValueError:
            raise HTTPException(status_code=400, detail="Formato de fecha inválido. Debe ser YYYY-MM-DD.")

        # Validar que los valores sean correctos
        if df["valor_compra"].isnull().any() or df["num_participaciones"].isnull().any():
            raise HTTPException(status_code=400, detail="No puede haber valores nulos en valor_compra o num_participaciones.")

        if (df["valor_compra"] < 0).any() or (df["num_participaciones"] < 0).any():
            raise HTTPException(status_code=400, detail="Los valores de compra y participaciones deben ser positivos.")

        # Insertar datos en la BD
        for _, row in df.iterrows():
            fondo = models.Fondo(
                nombre=row["nombre"],
                fecha_compra=row["fecha_compra"].date(),
                valor_compra=row["valor_compra"],
                num_participaciones=row["num_participaciones"]
            )
            db.add(fondo)
        db.commit()

        return {"message": "Archivo procesado y datos guardados correctamente"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error procesando el archivo: {str(e)}")