from pydantic import BaseModel, Field


class Album(BaseModel):
    id: int = Field(gt=0)
    title: str = Field(min_length=1)
    artist: str = Field(min_length=1)
    year: int = Field(ge=1900, le=2100)
    genre: str = Field(min_length=3)
