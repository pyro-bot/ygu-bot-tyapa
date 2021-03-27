from pony.orm import *

db = Database()

class UserProfile(db.Entity):
    is_new = Required(bool, default=True)
    target_name = Optional(str)
    is_watch = Required(bool, default=True)

