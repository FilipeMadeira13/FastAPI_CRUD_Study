from typing import List

from fastapi import APIRouter, HTTPException, Response, status

from app.crud.album import create_album as crud_create
from app.crud.album import delete_album as crud_delete
from app.crud.album import get_album_by_id, get_all_albums
from app.crud.album import update_album as crud_update
from app.database.memory import db_albums
from app.database.postgres import SessionLocal
from app.models.album_model import Album, AlbumCreate, AlbumSchema, AlbumUpdate

router = APIRouter()


@router.get("/albums", status_code=status.HTTP_200_OK, response_model=List[AlbumSchema])
async def list_albums():
    async with SessionLocal() as session:
        return await get_all_albums(session)


@router.get(
    "/albums/{album_id}", status_code=status.HTTP_200_OK, response_model=AlbumSchema
)
async def get_album(album_id: int):
    async with SessionLocal() as session:
        return await get_album_by_id(session, album_id)


@router.post("/albums", status_code=status.HTTP_201_CREATED, response_model=AlbumSchema)
async def create_album(album: AlbumCreate):
    async with SessionLocal() as session:
        async with session.begin():
            return await crud_create(session, album)


@router.put("/albums/{album_id}", status_code=status.HTTP_200_OK)
async def update_album(album_id: int, album: AlbumUpdate):
    async with SessionLocal() as session:
        async with session.begin():
            return await crud_update(session, album_id, album)


@router.delete("/albums/{album_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_album(album_id: int):
    async with SessionLocal() as session:
        async with session.begin():
            await crud_delete(session, album_id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
