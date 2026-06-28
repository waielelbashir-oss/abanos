from fastapi import FastAPI
from backend.database import engine

app = FastAPI()

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
