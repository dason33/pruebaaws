from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():#recibe variables dentro del () ej: nom: str
    return {"Hello": "World"}
