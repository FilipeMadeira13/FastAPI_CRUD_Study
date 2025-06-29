import asyncio
import sys

# ⚠️ Fix para Windows + asyncio + asyncpg
if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from app.database.postgres import Base, engine
from app.models.album_model import Album


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


asyncio.run(init_models())
