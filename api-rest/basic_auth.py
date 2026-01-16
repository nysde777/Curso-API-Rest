from fastapi import FastAPI
from fastapi import Depends
from fastapi.security import HTTPBasic
from fastapi import HTTPException
from fastapi import status

app = FastAPI()

security = HTTPBasic()

@app.get("/secure-basic")
def secure_basic(credentials: str = Depends(security)):
    if credentials.username != "admin":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario incorrecto"
        )
    if credentials.password != "1234":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Contraseña incorrecta"
        )
    return {
        "message": "Autenticacion basic Correcta"
    }
