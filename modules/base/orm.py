from pony.orm import *
from pony.orm.core import Entity, EntityMeta
from pony.py23compat import with_metaclass
from pathlib import Path

from pony.utils.utils import throw

COG_NAME = str(Path(__file__).parent.stem)
COG_NAME = COG_NAME[0].upper() + COG_NAME[1:]

class BotEntityMeta(EntityMeta):
    def __new__(meta, name, bases, cls_dict):
        if 'BotEntity' in globals():
            if '__slots__' in cls_dict: throw(TypeError, 'Entity classes cannot contain __slots__ variable')
            cls_dict['__slots__'] = ()
        if name == 'BotEntity':
            name = COG_NAME + name
        return super().__new__(meta, name, bases, cls_dict)

class BotEntity(Entity, metaclass=BotEntityMeta):
    pass

class BotDatabase(Database):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.Entity = type.__new__(BotEntityMeta, 'Entity', (BotEntity,), {})
        self.Entity._database_ = self
