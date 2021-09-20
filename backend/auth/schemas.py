__all__ = [
    'UserAuth',
]

from pydantic import BaseModel
from typing import Optional


class UserAuth(BaseModel):
    id: Optional[str]
    name: Optional[str]
    pwd: Optional[str]
    token: Optional[str]
