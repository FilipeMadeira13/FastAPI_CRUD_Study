from typing import Optional

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String

from app.database.postgres import Base


class Album(Base):
    __tablename__ = "albums"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    artist = Column(String, nullable=False)
    year = Column(Integer)
    genre = Column(String)


class AlbumUpdate(BaseModel):
    title: Optional[str] = None
    artist: Optional[str] = None
    year: Optional[int] = None
    genre: Optional[str] = None

    class Config:
        from_attributes = True


class AlbumSchema(BaseModel):
    id: int
    title: str
    artist: str
    year: Optional[int] = None
    genre: Optional[str] = None

    class Config:
        from_attributes = True

class AlbumCreate(BaseModel):
    title: str
    artist: str
    year: Optional[int] = None
    genre: Optional[str] = None

    class Config:
        from_attributes = True
