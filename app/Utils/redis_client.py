"""
Initialize an asynchronous Redis client.

- host: Redis server hostname (default "localhost")
- port: Redis server port (default 6379)
- db: Logical Redis database (default 0)
- decode_responses: Decode bytes to strings (default True)
"""


from redis.asyncio import Redis

redis = Redis(
    host="localhost",
    port=6379,
    db=0,
    decode_responses=True
)
