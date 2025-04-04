"""ICTA app, version 1, minimal app."""

from __future__ import annotations

import os
import socket

import redis.asyncio as redis
from fastapi import FastAPI
from pydantic import BaseModel
from redis import exceptions

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))

app = FastAPI()
redis_conn = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)


class TotalHits(BaseModel):
    """Model for total hits on the server."""

    hits: int | None = None
    hostname: str


async def get_hit_count() -> int | None:
    """Get total hits on the server."""
    try:
        return await redis_conn.incr("hits")
    except exceptions.ConnectionError as exc:
        print(f"Error connecting to Redis: {exc}")  # noqa: T201
        return None


@app.get("/hits", summary="Get total hits on the server", response_model=TotalHits)
async def get_total_hits() -> TotalHits:
    """Get total hits on the server."""
    count = await get_hit_count()
    return TotalHits(hits=count, hostname=socket.gethostname())
