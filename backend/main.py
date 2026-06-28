from fastapi import FastAPI
from backend.database import engine, Base
import backend.models

app = FastAPI()

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"status": "OK", "project": "Abanos"}


@app.get("/db-check")
def db_check():
    try:
        conn = engine.connect()
        conn.close()
        return {"database": "connected successfully"}
    except Exception as e:
        return {"database": "failed", "error": str(e)}
