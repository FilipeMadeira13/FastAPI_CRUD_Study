from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.album_model import Album as AlbumModel
from app.models.album_model import AlbumCreate, AlbumUpdate


async def get_all_albums(session: AsyncSession) -> list[AlbumModel]:
    result = await session.execute(select(AlbumModel))
    return result.scalars().all()


async def get_album_by_id(session: AsyncSession, album_id: int) -> AlbumModel | None:
    return await session.get(AlbumModel, album_id)


async def create_album(session: AsyncSession, album_data: AlbumCreate) -> AlbumModel:
    new_album = AlbumModel(**album_data.model_dump())
    session.add(new_album)
    return new_album


async def update_album(
    session: AsyncSession, album_id: int, album_data: AlbumUpdate
) -> AlbumModel | None:
    album_to_update = await session.get(AlbumModel, album_id)
    if not album_to_update:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Album não encontrado"
        )
    update_data = album_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(album_to_update, key, value)

    return album_to_update


async def delete_album(session: AsyncSession, album_id: int):
    album_to_delete = await session.get(AlbumModel, album_id)
    if not album_to_delete:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Album não encontrado"
        )
    await session.delete(album_to_delete)
