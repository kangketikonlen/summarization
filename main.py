from typing import Optional
from fastapi import FastAPI

from models.artikel import Artikel

from utils.summarization import sum_v1

app = FastAPI()


@app.get("/")
def read_root():
    return {"success": True, "results": "Ehe"}


@app.post("/sum_v1/")
def create_item(artikel: Artikel):
    summary = sum_v1(artikel.deskripsi)
    return summary


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
