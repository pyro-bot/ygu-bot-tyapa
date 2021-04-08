import discord
from modules.base.db import db
from .app import RaitingBot

def setup(bot):
    bot.add_cog(RaitingBot(bot))