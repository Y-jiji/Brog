from pydantic import BaseModel
from typing import Optional, List

__all__ = [
    'UserProfile',
]


class UserProfile(BaseModel):
    fields: Optional[List[int]]
