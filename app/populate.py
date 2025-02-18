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
            models.Fondo(nombre="Fondo Global", fecha_compra=date(2023, 1, 15), valor_compra=1000.50, num_participaciones=10),
            models.Fondo(nombre="Fondo Europa", fecha_compra=date(2022, 6, 20), valor_compra=2500.75, num_participaciones=25),
            models.Fondo(nombre="Fondo Tecnología", fecha_compra=date(2021, 9, 10), valor_compra=1500.00, num_participaciones=15),
        ]

        db.add_all(fondos_ejemplo)
        db.commit()
        print("Base de datos poblada con datos de ejemplo.")
    else:
        print("La base de datos ya tiene datos, no se ha realizado ninguna inserción.")

    db.close()

if __name__ == "__main__":
    populate_db()
