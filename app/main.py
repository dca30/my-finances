from fastapi import FastAPI
from database import engine
import models
from routers import fondos, upload, frontend
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.requests import Request


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(fondos.router)
app.include_router(upload.router)
app.include_router(frontend.router)


templates = Jinja2Templates(directory="templates")
