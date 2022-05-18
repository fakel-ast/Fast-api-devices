import aioredis

from core.config.settings import REDIS_URI


class ApiService:

    @staticmethod
    async def increment_anagram_count(*args, **kwargs) -> int:
        """Increment anagram count in redis"""
        redis = aioredis.from_url(REDIS_URI)
        return await redis.incr("anagram_count")


api_s = ApiService()
