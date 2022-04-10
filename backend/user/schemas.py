from pydantic import BaseModel
from typing import Optional, List

__all__ = [
    'UserProfile',
]


class UserProfile(BaseModel):
    fields_my: Optional[List[int]]
