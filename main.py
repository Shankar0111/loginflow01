from fastapi import FastAPI
from database import users_collection
from models import User

app = FastAPI(
    title="Login API",
    version="1.0.0"
)
@app.get("/")
def home():
    return {
        "message": "Welcome to Login API"
    }


@app.post("/signup")
def signup(user: User):

    existing_user = users_collection.find_one(
        {"email": user.email}
    )
    if existing_user:
        return {
            "message": "Email already exists"
        }
    new_user = {
        "name": user.name,
        "email": user.email,
        "password": user.password
    }
    users_collection.insert_one(new_user)
    return {
        "message": "User registered successfully"
    }


@app.post("/login")
def login(user: User):
    existing_user = users_collection.find_one(
        {
            "email": user.email,
            "password": user.password
        }
    )
    if not existing_user:
        return {
            "message": "Invalid Email or Password"
        }
    return {
        "message": f"Welcome {existing_user['name']}"
    }