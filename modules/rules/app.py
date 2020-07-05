from discord import member
from loguru import logger
import aiofiles
import discord
from discord.ext import commands
from pathlib import Path

BASEDIR = Path(__file__).parent
RESOURCES = BASEDIR / 'resources'


class RulesBot(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info(f'Cog {self.__cog_name__} on ready')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.send(await self._get_rules())

    @commands.group(name='rules',
                    aliases=['правила'],
                    pass_context=True,
                    invoke_without_command=True)
    async def cmd(self, ctx):
        await ctx.author.send(await self._get_rules())

    @cmd.command(name='read',
                aliases=['читать'])
    async def read(self, ctx):
        await ctx.author.send(await self._get_rules())
    
    async def _get_rules(self):
        async with aiofiles.open(RESOURCES / 'rules.txt', 'r', encoding='utf8') as f:
            return await f.read()