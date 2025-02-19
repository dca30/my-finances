from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
from datetime import date

# Crear la base de datos y las tablas si no existen
models.Base.metadata.create_all(bind=engine)

def populate_db():
    db: Session = SessionLocal()

    # Verificar si la tabla tiene datos
    if db.query(models.Fondo).first() is None:
        fondos_ejemplo = [
            models.Fondo(nombre="Fondo Tecnología", isin="AS67F8A7SD5F", participaciones=150, rentabilidad=0, invertido=1507.28, beneficio=164.73),
            models.Fondo(nombre="Fondo Europa", isin="UICASIUD8766G", participaciones=180, rentabilidad=1, invertido=8736.12, beneficio=800.21),
            models.Fondo(nombre="Fondo Global", isin="789SDAF879SA", participaciones=846, rentabilidad=2, invertido=4220.70, beneficio=365.99),
            
            models.Compra(fecha_compra=date(2021, 9, 12), isin="AS67F8A7SD5F", importe=200, participaciones=10),
            models.Compra(fecha_compra=date(2022, 3, 21), isin="UICASIUD8766G", importe=200, participaciones=25),
            models.Compra(fecha_compra=date(2023, 6, 30), isin="789SDAF879SA", importe=200, participaciones=15),
        ]

        db.add_all(fondos_ejemplo)
        db.commit()
        print("Base de datos poblada con datos de ejemplo.")
    else:
        print("La base de datos ya tiene datos, no se ha realizado ninguna inserción.")

    db.close()

if __name__ == "__main__":
    populate_db()
