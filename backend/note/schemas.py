__all__ = [
    'UserNote',
]

import email
from grpc import Status
from pydantic import BaseModel
from typing import Optional

from sympy import content


class UserNote(BaseModel):
    email: Optional[str]
    note_name: Optional[str]
    content: Optional[str]
