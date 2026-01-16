from fastapi import FastAPI
from fastapi import Header
from fastapi import HTTPException

app = FastAPI()

VALID_TOKEN = "token_secreto_123"

@app.get("/secure-bearer")
def secure_bearer(authorization: str = Header(None)):
    if authorization is None:
        raise HTTPException(
            status_code=401,
            detail="Header authorization no enviado"
        )
    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Formato Bearer incorrecto"
        )
    token = authorization.replace("Bearer ", "")
    if token != VALID_TOKEN:
        raise HTTPException(
            status_code=401,
            detail="Token invalido"
        )

    return {
        "message": "Acceso concedido con Bearer Token"
    }