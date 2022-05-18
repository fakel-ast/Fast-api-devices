import random

import aioredis

from core.config.settings import REDIS_URI
from core.apps.api.models import Devices, Endpoint


class ApiService:
    model = Devices
    endpoint_model = Endpoint

    @staticmethod
    async def increment_anagram_count(*args, **kwargs) -> int:
        """Increment anagram count in redis"""
        redis = aioredis.from_url(REDIS_URI)
        return await redis.incr("anagram_count")

    async def insert_devices(self, types: list, *args, **kwargs) -> bool:
        """Insert devices and endpoints"""

        # save Device. We can't use bulk create because of that we must have id :(
        devices = [
            await self.model.create(dev_id=self.generate_mac_address(), dev_type=random.choice(types))
            for _ in range(10)
        ]

        # bulk create endpoints
        endpoints = [
            self.endpoint_model(device=device) for device in random.sample(devices, 5)
        ]
        await self.endpoint_model.bulk_create(endpoints)

        return True

    @staticmethod
    def generate_mac_address(*args, **kwargs) -> str:
        # https://gist.github.com/pklaus/9638536
        return "%02x:%02x:%02x:%02x:%02x:%02x" % (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )


api_s = ApiService()
