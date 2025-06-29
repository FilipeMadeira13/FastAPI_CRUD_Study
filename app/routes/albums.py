from fastapi import APIRouter, HTTPException, Response, status

from app.database.memory import db_albums
from app.models.album import Album

router = APIRouter()


@router.get("/albums", status_code=status.HTTP_200_OK)
async def list_albums() -> list[Album]:
    """Lista todos os álbuns.

    Returns:
        list[Album]: A lista completa dos álbuns.
    """
    return db_albums


@router.get("/albums/{album_id}", status_code=status.HTTP_200_OK)
async def get_album(album_id: int) -> Album:
    """Retorna um album pelo seu id.

    Args:
        album_id (int): id do álbum

    Raises:
        HTTPException: Exceção levantada quando o álbum não é encontrado.

    Returns:
        Album: um álbum localizado pelo seu id.
    """
    for album in db_albums:
        if album.id == album_id:
            return album
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Álbum com ID {album_id} não encontrado"
    )


@router.post("/albums", status_code=status.HTTP_201_CREATED)
async def create_album(album: Album) -> Album:
    """Cria um álbum e adiciona-o a lista.

    Args:
        album (Album): classe Album com todos os seus campos para serem editados.

    Raises:
        HTTPException: Exceção levantada se o álbum com o id já existe.

    Returns:
        Album: O álbum criado.
    """
    if any(a.id == album.id for a in db_albums):
        raise HTTPException(status_code=400, detail="ID já existente")
    db_albums.append(album)
    return album


@router.put("/albums/{album_id}", status_code=status.HTTP_200_OK)
async def update_album(album_id: int, album: Album) -> Album:
    """Atualiza um ou mais campos de um álbum localizado pelo seu id.

    Args:
        album_id (int): id do album
        album (Album): o album para ser editado

    Raises:
        HTTPException: Exceção levantada se o álbum a ser editado não foi encontrado.

    Returns:
        Album: O álbum atualizado.
    """
    for i, a in enumerate(db_albums):
        if a.id == album_id:
            db_albums[i] = album
            return album
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Álbum com ID {album_id} não encontrado"
    )


@router.delete("/albums/{album_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_album(album_id: int):
    """Remove um álbum da lista

    Args:
        album_id (int): id do álbum

    Raises:
        HTTPException: Exceção levantada se o álbum a ser excluído não foi encontrado.

    Returns:
        Uma mensagem informando que a exclusão foi bem sucedida.
    """
    for i, a in enumerate(db_albums):
        if a.id == album_id:
            db_albums.pop(i)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Álbum com ID {album_id} não encontrado"
    )
