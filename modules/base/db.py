# from . import orm
from pony import orm
import settings

db = orm.Database()
orm.set_sql_debug(settings.DEBUG)