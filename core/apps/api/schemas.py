from typing import Optional

from pydantic import BaseModel, Field


class CheckAnagram(BaseModel):
    string_one: str
    string_two: str


class CheckAnagramResponse(BaseModel):
    is_anagram: bool
    anagram_count: Optional[int]


class DeviceCount(BaseModel):
    dev_type: str
    count: int


class GetDevicesCount(BaseModel):
    __root__: list[DeviceCount]
