from fastapi import FastAPI
from fastapi import Header
from fastapi import HTTPException

app = FastAPI()

VALID_API_KEY = "mi_api_key_secreta"

@app.get("/secure-api-key")
def secure_api_key(x_api_key: str = Header(None)):
    if x_api_key is None:
        raise HTTPException(
            status_code=401,
            detail="API key no enviada"
        )
    if x_api_key != VALID_API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Api key es Invalida"
        )
    
    return {
        "message": "Acceso concedido con la API KEY"
    }