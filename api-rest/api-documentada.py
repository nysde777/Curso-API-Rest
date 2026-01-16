from fastapi import FastAPI
from fastapi import HTTPException

app = FastAPI(
    title="API de usuarios",
    description="API para gestionar usuarios con autenticación básica",
    version="1.0.0"
)

users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]

@app.get(
    "/users",
    summary="Obtener lista de usuarios",
    description="Devuelve una lista de todos los usuarios registrados en el sistema."
)
def get_users():
    return users

@app.get(
    "/users/{user_id}",
    summary="Obtener usuario por ID",
    description="Devuelve los detalles de un usuario específico dado su ID."
)
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )

@app.post(
    "/users",
    summary="Crear un nuevo usuario",
    description="Crea un nuevo usuario con el nombre proporcionado."
)
def create_user(user: dict):
    if "name" not in user:
        raise HTTPException(
            status_code=400,
            detail="El campo 'name' es obligatorio"
        )
    new_id = users[-1]["id"] + 1
    new_user = {"id": new_id, "name": user["name"]}
    users.append(new_user)
    return new_user