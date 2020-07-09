import discord
from .app import FirstContactBot

def setup(bot):
    bot.add_cog(FirstContactBot(bot))