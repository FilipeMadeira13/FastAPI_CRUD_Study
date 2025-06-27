from pydantic import BaseModel, Field


class Album(BaseModel):
    """Classe representando um álbum de música

    Args:
        BaseModel (class): Modelo Base para o padrão a ser seguido.
    """

    id: int = Field(gt=0)
    title: str = Field(min_length=1)
    artist: str = Field(min_length=1)
    year: int = Field(ge=1900, le=2100)
    genre: str = Field(min_length=3)
