from fastapi import APIRouter, HTTPException, status

from app.database import db_albums
from app.models import Album

router = APIRouter()


@router.get("/albums", status_code=status.HTTP_200_OK)
async def list_albums():
    return db_albums


@router.get("/albums/{album_id}", status_code=status.HTTP_200_OK)
async def get_album(album_id: int):
    for album in db_albums:
        if album.id == album_id:
            return album
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Álbum não encontrado"
    )


@router.post("/albums", status_code=status.HTTP_201_CREATED)
async def create_album(album: Album):
    db_albums.append(album)
    return album


@router.put("/albums/{album_id}", status_code=status.HTTP_200_OK)
async def update_album(album_id: int, album: Album):
    for i, a in enumerate(db_albums):
        if a.id == album_id:
            db_albums[i] = album
            return album
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Álbum não encontrado"
    )


@router.delete("/albums/{album_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_album(album_id: int):
    for i, a in enumerate(db_albums):
        if a.id == album_id:
            db_albums.pop(i)
            return {"message": "Deleted"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Álbum não encontrado"
    )
