from pydantic import BaseModel, Field


class Album(BaseModel):
    id: int = Field(gt=0)
    title: str = Field(min_length=1)
    artist: str = Field(min_length=1)
