from enum import Enum
from typing import Union

from pony.orm.core import PrimaryKey
from . import db
from pony import orm

class Penalty(db.Entity):

    class OBJ_TYPE(Enum):
        STUD = 'stud'
        GROUP = 'group'

    id = orm.PrimaryKey(int, auto=True)
    target = orm.Required(str)
    target_type = orm.Required(str)
    msg = orm.Optional(str, nullable=True)
    author = orm.Required(str)

