from datetime import datetime, date, timedelta
from typing import List, Dict, Any
from db import get_db, COLLECTION_NAME

async def upsert_usage(client_id: int):
    db = get_db()
    today_str = datetime.utcnow().strftime("%Y-%m-%d")
    result = await db[COLLECTION_NAME].update_one(
        {"client_id": client_id, "day": today_str},
        {"$inc": {"usage_count": 1}},
        upsert=True
    )
    return result

async def get_usage_stats(client_id: int, start_date: date, end_date: date) -> Dict[str, Any]:
    db = get_db()
    start_date_str = start_date.strftime("%Y-%m-%d")
    end_date_str = end_date.strftime("%Y-%m-%d")
    
    cursor = db[COLLECTION_NAME].find({
        "client_id": client_id,
        "day": {"$gte": start_date_str, "$lte": end_date_str}
    }).sort("day", 1)
    
    daily_uses: List[Dict[str, Any]] = []
    total_usage = 0

    async for doc in cursor:
        count = doc.get("usage_count", 0)
        total_usage += count
        daily_uses.append({"date": doc["day"], "count": count})
    
    return {"last_month_use": total_usage, "daily_uses": daily_uses}
