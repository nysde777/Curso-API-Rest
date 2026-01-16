from fastapi import FastAPI
from fastapi import HTTPException

app = FastAPI()

users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

@app.get("/users")
def get_users():
    return users

@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
        
    raise HTTPException(
        status_code=404, 
        detail="Usuario no existe"
    )

@app.post("/users")
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

