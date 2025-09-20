# test_redis.py
from redis.asyncio import Redis
import asyncio

async def main():
    redis = Redis(host="localhost", port=6379, db=0, decode_responses=True)
    await redis.set("test_key", "Hello Redis!")
    value = await redis.get("test_key")
    print("Value from Redis:", value)
    await redis.aclose()

asyncio.run(main())
