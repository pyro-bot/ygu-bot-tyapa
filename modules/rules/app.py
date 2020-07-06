from discord import member
from loguru import logger
import aiofiles
import discord
from discord.ext import commands
from modules.base.ext import BaseBot
import re


class RulesBot(BaseBot):

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.send("Здравствуйте, это бот сервера 58281-2018 к которому вы только что присоединились. Пожалуйста перед тем как что либо делать на сервера прочтите правила.")
        await self._send_rule(member)

    @commands.group(name='rules',
                    aliases=['rule', 'правила'],
                    pass_context=True,
                    invoke_without_command=True)
    async def cmd(self, ctx):
        await self._send_rule(ctx.author)

    @cmd.command(name='read',
                aliases=['читать'])
    async def read(self, ctx):
        await self._send_rule(ctx.author)
    
    async def _send_rule(self, chat):
        rules = await self._get_rules()
        for num, rule in enumerate(re.split('\n\n[2-9]\. ', rules), 1):
            if num == 1:
                await chat.send(rule)
            else:
                await chat.send(f'{num}. {rule}')

    async def _get_rules(self):
        async with aiofiles.open(self.RESOURCES / 'rules.txt', 'r', encoding='utf8') as f:
            return await f.read()