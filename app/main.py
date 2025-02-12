from fastapi import FastAPI
from app.database import init_db

app = FastAPI()

@app.on_event("startup")
def startup():
    init_db()
