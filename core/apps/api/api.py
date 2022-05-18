from fastapi import APIRouter, status

from core.apps.api import schemas
from core.apps.api.service import api_s

api_router = APIRouter()


@api_router.post('/check-anagram/', response_model=schemas.CheckAnagramResponse)
async def check_anagram(check_data: schemas.CheckAnagram) -> schemas.CheckAnagramResponse:
    return_data = {
        'is_anagram': sorted(check_data.string_one) == sorted(check_data.string_two)
    }
    if return_data.get('is_anagram'):
        return_data['anagram_count'] = await api_s.increment_anagram_count()
    return schemas.CheckAnagramResponse.parse_obj(return_data)


@api_router.post('/devices/', status_code=status.HTTP_201_CREATED)
async def insert_devices():
    device_types = ['emeter', 'zigbee', 'lora', 'gsm']
    await api_s.insert_devices(types=device_types)
    return True


@api_router.get('/devices/', response_model=schemas.GetDevicesCount)
async def get_devices():
    devices_count = await api_s.get_devices_count()
    return schemas.GetDevicesCount.parse_obj(devices_count)
