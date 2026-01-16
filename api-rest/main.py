from fastapi import FastAPI

app = FastAPI()

@app.get("/user")
def get_user():
    return {
        "id": 1,
        "name": "Ana",
        "active": True
    }

