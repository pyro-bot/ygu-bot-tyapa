from discord import member
from loguru import logger
import aiofiles
import discord
from discord.ext import commands
from modules.base.ext import BaseBot
import re


class ExampleBot(BaseBot):
    """
    Это пример бота. Он умеет ходить домой
    Если вам нужен более продвинутый пример посмотрите модуль rules
    """

    # хук на событие подключения пользователя к серверу
    # имя события задаются с помошью названия функции
    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.send("Здравствуйте, вы только что зашли на сервер")
        await self._send_rule(member)

    # Создание группы команд c yfpdfybtv go
    @commands.group(name='go',
                    aliases=['идти'],
                    pass_context=True,
                    invoke_without_command=True)
    async def cmd_group(self, ctx):
        await ctx.send("""Куда идти?
        Для того чтобы пойти домой напишите в чате
        >go home или >идти домой""")

    # Одна из команд в группе
    @cmd_group.command(name='home',
                aliases=['домой'])
    async def got_to_home(self, ctx):
        await ctx.author.send("Идем домой")