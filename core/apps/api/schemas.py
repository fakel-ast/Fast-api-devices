from typing import Optional

from pydantic import BaseModel


class CheckAnagram(BaseModel):
    string_one: str
    string_two: str


class CheckAnagramResponse(BaseModel):
    is_anagram: bool
    anagram_count: Optional[int]
