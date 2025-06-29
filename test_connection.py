import asyncpg
import asyncio

async def test():
    try:
        conn = await asyncpg.connect(
            user="cfili",
            password="senha",
            database="music_db",
            host="localhost"
        )
        print("✅ Conexão bem-sucedida!")
        await conn.close()
    except Exception as e:
        print(f"❌ Erro: {e}")

asyncio.run(test())