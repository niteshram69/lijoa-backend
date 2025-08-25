from fastapi import FastAPI
from app.db import db_ok
app = FastAPI(title="LIJOA API", version="0.1.0")
@app.get("/healthz")
def healthz():
# checks DB connectivity as part of health
    try:
        db_ok()
        return {"status": "ok", "db": "ok"}
    except Exception as e:
        return {"status": "degraded", "db": f"error: {e.__class__.__name__}"}
