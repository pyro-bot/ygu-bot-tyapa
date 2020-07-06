import settings
from loguru import logger
import discord
import discord.ext.commands
from bot import DiscordBot

logger.configure(**settings.LOGGING)

bot = DiscordBot('>')

for module_name in settings.MODULES:
    bot.load_extension('modules.' + module_name)    

if __name__ == "__main__":
    bot.run(settings.TOKEN)