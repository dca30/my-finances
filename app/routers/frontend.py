from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import SessionLocal
import models

router = APIRouter()

# Configurar Jinja2 para renderizar plantillas desde /templates
templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.get("/")
async def homepage(request: Request, db: Session = Depends(get_db)):
    fondos = db.query(models.Fondo).all()
    return templates.TemplateResponse("index.html", {"request": request, "fondos": fondos})