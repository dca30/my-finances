from datetime import date
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

"""class ChoiceBase(BaseModel):
    choice_text: str
    is_correct:bool
    
class QuestionBase(BaseModel):
    question_text: str
    choices: List[ChoiceBase]"""
    
class FondoBase(BaseModel):
    nombre: str
    fecha_compra: date
    valor_compra: float
    num_participaciones: float
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependency = Annotated[Session, Depends(get_db)]


"""@app.get("/questions/{question_id}")
async def read_question(question_id: int, db: db_dependency):
    result = db.query(models.Questions).filter(models.Questions.id == question_id).first()
    if not result:
        raise HTTPException(status_code=404, detail='Question not found')
    return result


@app.post("/questions/")
async def create_questions(question: QuestionBase, db: db_dependency):
    db_question = models.Questions(question_text=question.question_text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    for choice in question.choices:
        db_choice = models.Choices(choice_text=choice.choice_text, is_correct=choice.is_correct, question_id=db_question.id)
        db.add(db_choice)
    db.commit()"""

@app.get("/fondos/{fondo_id}")
async def read_fondo(fondo_id: int, db: db_dependency):
    result = db.query(models.Fondo).filter(models.Fondo.id == fondo_id).first()
    if not result:
        raise HTTPException(status_code=404, detail='Fondo not found')
    return result

@app.post("/fondos/")
async def create_fondo(fondo: FondoBase, db: db_dependency):
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