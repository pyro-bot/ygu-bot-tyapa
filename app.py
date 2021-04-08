import settings
from loguru import logger
import discord
import discord.ext.commands
from bot import DiscordBot

logger.configure(**settings.LOGGING)

bot = DiscordBot('>')

for module_name in settings.MODULES:
    bot.load_extension('modules.' + module_name)    

from modules.base.db import db
db.bind(**settings.DATABASE)
db.generate_mapping(create_tables=True)

if __name__ == "__main__":
    bot.run(settings.TOKEN)