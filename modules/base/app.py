import aiofiles
from pathlib import Path
from modules.base.ext import BaseBot
from discord.ext import commands

class MainBot(BaseBot):

    @commands.command(name='about',
                aliases=['описание'])
    async def about(self, ctx):
        await ctx.send("Описание бота")
