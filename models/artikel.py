from pydantic import BaseModel


class Artikel(BaseModel):
    deskripsi: str


class ArtkelV2(BaseModel):
    url: str
