from datetime import datetime
from typing import Dict
from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def root() -> str:
    return "Pong"