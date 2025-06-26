from pydantic import BaseModel


class Album(BaseModel):
    id: int
    title: str
    artist: str
