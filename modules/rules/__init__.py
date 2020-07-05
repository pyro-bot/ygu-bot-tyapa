import discord
from .app import RulesBot

def setup(bot):
    bot.add_cog(RulesBot(bot))