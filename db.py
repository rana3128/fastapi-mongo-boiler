import os
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI
from contextlib import asynccontextmanager

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "testdb")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "usage_stats")

mongo_client: AsyncIOMotorClient = None
mongo_db = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global mongo_client, mongo_db
    mongo_client = AsyncIOMotorClient(MONGO_URI)
    mongo_db = mongo_client[DATABASE_NAME]
    await mongo_db[COLLECTION_NAME].create_index(
        [("client_id", 1), ("day", 1)], unique=True
    )
    print("Connected to MongoDB and ensured index exists.")
    yield
    mongo_client.close()
    print("MongoDB connection closed.")

def get_db():
    return mongo_db
