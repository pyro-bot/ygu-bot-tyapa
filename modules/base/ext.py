from discord import member
from loguru import logger
import aiofiles
import discord
from discord.ext import commands
from pathlib import Path
import importlib.util


class BaseBotMeta(commands.CogMeta):
    
    def __new__(cls, *args, **kwargs):
        name, bases, attrs = args
        new_cls = super().__new__(cls, name, bases, attrs, **kwargs)
        module = importlib.util.find_spec(new_cls.__module__)
        
        new_cls.BASEDIR = Path(str(module.origin)).parent
        new_cls.RESOURCES = new_cls.BASEDIR / 'resources'
        new_cls.RESOURCES.mkdir(exist_ok=True)

        new_cls.logger = logger
        return new_cls


class BaseBot(commands.Cog, metaclass=BaseBotMeta):
    """
    Доступны поля:
    BASEDIR - содержить объект Path, указывающий на папку модуля
    RESOURCES - содержить объект Path, указывающий на папку ресурсов модуля (папка гарантирована существует)
    """

    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.Cog.listener()
    async def on_ready(self):
        self.logger.info(f'Cog {self.__cog_name__} on ready')
