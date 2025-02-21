from fastapi import FastAPI, Depends, BackgroundTasks
from datetime import date
from db import lifespan
from query import upsert_usage, get_usage_stats

app = FastAPI(lifespan=lifespan)

@app.get("/product/{client_id}")
async def product_endpoint(client_id: int, background_tasks: BackgroundTasks):
    background_tasks.add_task(upsert_usage, client_id)
    return {
        "client_id": client_id,
        "message": f"Usage for client {client_id} will be incremented in background."
    }

@app.get("/stats/{client_id}")
async def stats_endpoint(
    client_id: int, 
    start_date: date = None, 
    end_date: date = None
):
    if start_date is None:
        start_date = date.today().replace(day=1)
    if end_date is None:
        end_date = date.today()
    
    stats = await get_usage_stats(client_id, start_date, end_date)
    return stats
