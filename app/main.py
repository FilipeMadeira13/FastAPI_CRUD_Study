from fastapi import FastAPI

from app.model_fake import Album

app = FastAPI()

db_albums = []


@app.get("/")
async def root():
    return {"message": "API funcionando!"}


@app.get("/albums")
async def list_albums():
    return db_albums


@app.post("/albums")
async def create_album(album: Album):
    db_albums.append(album)
    return album


@app.put("/albums/{album_id}")
async def update_album(album_id: int, album: Album):
    for i, a in enumerate(db_albums):
        if a.id == album_id:
            db_albums[i] = album
            return album
    return {"error": "Album not found"}


@app.delete("/albums/{album_id}")
async def delete_album(album_id: int):
    for i, a in enumerate(db_albums):
        if a.id == album_id:
            db_albums.pop(i)
            return {"message": "Deleted"}
    return {"error": "Album not found"}
