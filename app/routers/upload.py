from datetime import datetime
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

# Columnas esperadas en el nuevo CSV
EXPECTED_COLUMNS = {"Fecha de la orden", "ISIN", "Importe estimado", "Nº de participaciones"}

@router.post("/upload_csv/")
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        # Leer CSV con separador ";"
        df = pd.read_csv(file.file, delimiter=";")

        # Validar columnas
        if not EXPECTED_COLUMNS.issubset(df.columns):
            raise HTTPException(status_code=400, detail=f"El CSV debe contener las columnas: {EXPECTED_COLUMNS}")

        # Eliminar filas donde la columna Estado contenga "Rechazada"
        df = df[~df["Estado"].str.contains("Rechazada", na=False)]

        
        # Convertir fecha a formato datetime
        try:
            df["Fecha de la orden"] = pd.to_datetime(df["Fecha de la orden"], format="%d/%m/%Y")
        except ValueError:
            raise HTTPException(status_code=400, detail="Formato de fecha inválido. Debe ser DD/MM/YYYY.")
        
        # Limpiar "Importe estimado" (quitar " EUR" y cambiar "," por ".")
        df["Importe estimado"] = df["Importe estimado"].str.replace(" EUR", "", regex=False).str.replace(",", ".").astype(float)
        
        # Limpiar "Nº de participaciones" (cambiar "," por ".")
        df["Nº de participaciones"] = df["Nº de participaciones"].str.replace(",", ".").astype(float)

        # Validar valores
        if df["Importe estimado"].isnull().any() or df["Nº de participaciones"].isnull().any():
            raise HTTPException(status_code=400, detail="No puede haber valores nulos en Importe estimado o Nº de participaciones.")

        if (df["Importe estimado"] < 0).any() or (df["Nº de participaciones"] < 0).any():
            raise HTTPException(status_code=400, detail="Los valores de Importe estimado y Nº de participaciones deben ser positivos.")

        # Insertar datos en la BD
        for _, row in df.iterrows():
            compra = models.Compra(
                fecha_compra=row["Fecha de la orden"].date(),
                isin=row["ISIN"],
                importe=row["Importe estimado"],
                participaciones=row["Nº de participaciones"]
            )
            db.add(compra)

        db.commit()
        return {"message": "Archivo procesado y datos guardados correctamente"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error procesando el archivo: {str(e)}")
