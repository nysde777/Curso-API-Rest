from fastapi import FastAPI
from datetime import datetime
from datetime import timezone

app = FastAPI()

@app.get("/text")
def get_text():
    return {
        "mensaje": "José Pérez – APIs y programación - año"
    }

@app.get("/time")
def get_time():
    now = datetime.now(timezone.utc)
    iso_date = now.isoformat()

    return {
        "tiempo": iso_date
    }