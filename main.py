from fastapi import FastAPI, HTTPException, status
from models.db import db
from models.models import Sheep
from typing import List

app = FastAPI()

@app.get("/sheep/{sheep_id}", response_model=Sheep)
def get_sheep(sheep_id: int):
    sheep = db.get_sheep(sheep_id)
    if sheep is None:
        raise HTTPException(status_code=404, detail="Sheep not found")
    return sheep

@app.post("/sheep", response_model=Sheep, status_code=status.HTTP_201_CREATED)
def add_sheep(sheep: Sheep):
    db.add_sheep(sheep)
    return sheep

@app.delete("/sheep/{sheep_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sheep(sheep_id: int):
    result = db.delete_sheep(sheep_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Sheep not found")
    return

@app.put("/sheep/{sheep_id}", response_model=Sheep)
def update_sheep(sheep_id: int, sheep: Sheep):
    updated = db.update_sheep(sheep_id, sheep)
    if updated is None:
        raise HTTPException(status_code=404, detail="Sheep not found")
    return updated

@app.get("/sheep", response_model=List[Sheep])
def get_all_sheep():
    return db.get_all_sheep() 