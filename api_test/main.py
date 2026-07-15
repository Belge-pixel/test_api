from fastapi import FastAPI
from .data import users
from typing import List,Dict


app = FastAPI()

@app.get("/")
def root():
    
    return {
        "message":"The App is running"
    }

app.get("/users")    
def get_users()->Dict[List]:
    return users       