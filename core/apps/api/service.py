import random

import aioredis
from tortoise.expressions import RawSQL
from tortoise.functions import Count

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

    async def get_devices_count(self, *args, **kwargs) -> list:
        # Это пиздец на самом деле.
        # Я кнч знал что тортила не самая лучшая орм, но тут даже group_by не работает.
        # Я его и так, и сяк писал, но он его просто не видел. Так еще и в сырой запрос нельзя (у меня не получилось)
        # засунуть свои поля. В итоге пришлось count называть как id.
        # лучше бы на алхимии писал))
        devices_count = await self.model.raw(
            'select devices.dev_type, COUNT(devices.id) AS "id" from devices '
            'JOIN endpoint ON endpoint.device_id = devices.id '
            'GROUP BY devices.dev_type '
        )
        # Гений парсинга снова в деле. У raw нельзя использовать values))
        return [{'count': device.id, 'dev_type': device.dev_type} for device in devices_count]

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
