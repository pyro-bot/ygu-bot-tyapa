import discord
from .app import MainBot

def setup(bot):
    bot.add_cog(MainBot(bot))