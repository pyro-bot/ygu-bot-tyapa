import discord
from .app import ExampleBot

def setup(bot):
    bot.add_cog(ExampleBot(bot))