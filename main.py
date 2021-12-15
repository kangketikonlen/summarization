from typing import Optional
from fastapi import FastAPI

from models.artikel import Artikel, ArtkelV2

from utils.summarization import sum_v1, sum_v2, sum_v3

app = FastAPI()


@app.get("/")
def read_root():
    return {"success": True, "results": "Ehe"}


@app.post("/sumv1/")
def create_item(artikel: Artikel):
    summary = sum_v1(artikel.deskripsi)
    return {"success": True, "results": summary}


@app.post("/sumv2/")
def create_item(url: ArtkelV2):
    summary = sum_v2(url.url)
    return {"success": True, "results": summary}


@app.post("/sumv3/")
def create_item(artikel: Artikel):
    summary = sum_v3(artikel.deskripsi)
    return {"success": True, "results": summary}
