from operator import mod
import settings
from loguru import logger
import discord
import discord.ext.commands

logger.configure(**settings.LOGGING)

bot = discord.ext.commands.Bot('>')

for module_name in  settings.MODULES:
    # module = __import__('modules.' + module_name)
    bot.load_extension('modules.' + module_name)
    

bot.run(settings.TOKEN)