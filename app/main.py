from fastapi import FastAPI
from models import Employee,Asset
import models
from routes import router
from config import engine
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router, prefix="", tags=["employee"])

