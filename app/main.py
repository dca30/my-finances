from fastapi import FastAPI
from database import engine
import models
from routers import fondos, upload

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(fondos.router)
app.include_router(upload.router)