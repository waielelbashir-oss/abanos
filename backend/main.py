from fastapi import FastAPI

app = FastAPI(title="Abanos API", version="0.1.0")

@app.get("/")
def home():
    return {"message": "Abanos API is running"}

@app.get("/health")
def health():
    return {
        "status": "OK",
        "project": "Abanos",
        "version": "0.1.0"
    }
