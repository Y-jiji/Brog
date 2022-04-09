from _ext.sqlalchemy import *
from .models import Field


def getAvaliableFields():
    field_list = db.query(Field).all()
    return field_list


async def addAvailableField(name):
    field_obj = Field(name=name)
    db.add(field_obj)
    db.commit()
