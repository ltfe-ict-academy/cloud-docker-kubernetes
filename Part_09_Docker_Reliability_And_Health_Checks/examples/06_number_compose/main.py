"""ICTA app, version 1, minimal app."""

from __future__ import annotations

import os
import random
import socket

import redis.asyncio as redis
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from redis import exceptions

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
SIMULATE_ERROR: bool = bool(os.getenv("SIMULATE_ERROR", "true").lower() == "true")

app = FastAPI()
redis_conn = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
count = 0


class TotalHits(BaseModel):
    """Model for total hits on the server."""

    hits: int | None = None
    hostname: str


class RandomNumber(BaseModel):
    """Model for random number."""

    number: int


class HealthCheck(BaseModel):
    """Model for health check."""

    status: str


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


@app.get("/rng", summary="Get random number", response_model=RandomNumber)
async def get_random_number() -> RandomNumber:
    """Get random number."""
    number = random.randint(1, 100)  # noqa: S311
    global count  # noqa: PLW0603
    count += 1
    if SIMULATE_ERROR and count > 5:  # noqa: PLR2004
        raise HTTPException(status_code=500, detail="Internal server error")
    return RandomNumber(number=number)


@app.get("/health", summary="Health check", response_model=HealthCheck)
async def health_check() -> HealthCheck:
    """Health check."""
    global count  # noqa: PLW0602
    if SIMULATE_ERROR and count > 5:  # noqa: PLR2004
        raise HTTPException(status_code=500, detail="Internal server error")
    return HealthCheck(status="ok")
