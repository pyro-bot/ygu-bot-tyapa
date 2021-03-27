import sys
import os
DEBUG = bool(os.environ.get('DEBUG', False))
TOKEN = os.environ.get('TOKEN')

MODULES = (
    'base',
    # 'rules',
    # 'firstcontact',
    # 'example'
)

LOGGING = {
    "handlers": [
        {"sink": sys.stdout, "format": "{time} - {message}"},
        {"sink": "logs/info.log", 'level': 'INFO', 'retention': '1 days'},
        {"sink": "logs/error.log", 'level': 'ERROR', 'rotation': '1 week'},
    ],
    "extra": {"user": "someone"}
}


# Это должно быть в самом конце файла и после этого блока конец файла
if not DEBUG:
    from settings_prod import *