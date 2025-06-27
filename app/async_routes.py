import asyncio

from fastapi import APIRouter

router = APIRouter()


@router.get("/simples-sync")
def sync_simulation():
    import time

    time.sleep(2)
    return {"msg": "Processo síncrono finalizado"}


@router.get("/simples-async")
async def async_simulation():
    await asyncio.sleep(2)
    return {"msg": "Processo assíncrono finalizado"}


@router.get("/paralelo")
async def tarefa_paralela():
    async def tarefa(n):
        await asyncio.sleep(n)
        return f"Tarefa {n}s finalizada"

    resultados = await asyncio.gather(tarefa(2), tarefa(3), tarefa(1))

    return {"resultados": resultados}


@router.get("/comparar")
async def comparar_execucoes():
    import time

    start = time.perf_counter()
    await asyncio.sleep(2)  # Troca por time.sleep para comparar resultados
    # time.sleep(2)
    elapsed = time.perf_counter() - start

    return {"tempo_gasto": elapsed}
