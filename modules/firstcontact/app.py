from discord import member
from loguru import logger
import aiofiles
import asyncio
from discord.ext import commands
from modules.base.ext import BaseBot
from . import model


class FirstContactBot(BaseBot):
    """
    Управление новыми пользователями
    """

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await asyncio.sleep(10)
        await member.send("""Здравствуйте, вы недавно присоеденились в серверу, пожалуйства преставитесь
        Написав в данном чате
        >fc im Фимилия Имя Отчество номер_группы
        Например
        >fc im Иванов Иван Иванович 1121б""")
        await self._send_rule(member)

    # Создание группы команд c yfpdfybtv go
    @commands.group(name='fc',
                    aliases=['firstcontact', 'first_contact', 'первыйконтакт', 'пк', 'первый_контакт'],
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