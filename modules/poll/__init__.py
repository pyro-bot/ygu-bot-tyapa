import discord
from .app import PollBot

def setup(bot):
    bot.add_cog(PollBot(bot))