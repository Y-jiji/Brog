from _ext.sqlalchemy import Base, engine
from auth.models import *

create_all = lambda : Base.metadata.create_all(engine)
drop_all = lambda : Base.metadata.drop_all(engine)