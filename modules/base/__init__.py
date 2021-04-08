import discord
# from . import orm
from . import db
from .app import MainBot


def setup(bot):
    bot.add_cog(MainBot(bot))