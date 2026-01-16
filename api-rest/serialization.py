from fastapi import FastAPI
from fastapi import Request

app = FastAPI()

@app.post("/users")
async def create_user(request: Request):
    data = await request.json()
    return {
        "data_recibida": data
    }

