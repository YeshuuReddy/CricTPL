import json
import functools
from typing import Callable, Any
from app.Utils.redis_client import redis

def redis_cache(ttl: int = 60):
    """
    Decorator to cache function results in Redis.
    Works with SQLAlchemy ORM objects too.
    """
    def decorator(func: Callable):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs) -> Any:
            key_parts = [func.__name__] + list(map(str, args)) + [f"{k}={v}" for k, v in kwargs.items()]
            cache_key = ":".join(key_parts)

            # Check cache
            cached = await redis.get(cache_key)
            if cached:
                return json.loads(cached)

            # Execute function
            result = await func(*args, **kwargs)

            # Handle SQLAlchemy ORM serialization
            if isinstance(result, list) and result and hasattr(result[0], "__dict__"):
                result_to_cache = [obj.__dict__.copy() for obj in result]
                for r in result_to_cache:
                    r.pop("_sa_instance_state", None)
            elif hasattr(result, "__dict__"):
                result_to_cache = result.__dict__.copy()
                result_to_cache.pop("_sa_instance_state", None)
            else:
                result_to_cache = result

            # Save to Redis
            await redis.set(cache_key, json.dumps(result_to_cache), ex=ttl)
            return result_to_cache
        return wrapper
    return decorator
