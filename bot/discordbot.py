import asyncio
from loguru import logger
import discord
import discord.ext.commands
from discord.channel import ChannelType

DESCRIPTION = """Данный бот предназначен для реализации широкого спектра функций на сервере 58281-2018.
Если вы желаете принять участи в разработке бота, то вам сюда https://github.com/pyro-bot/ygu-bot-tyapa
"""

class DiscordBot(discord.ext.commands.Bot):

    def __init__(self, *args, **kwargs):
        kwargs['description'] = DESCRIPTION
        super().__init__(*args, **kwargs)
    
    async def process_commands(self, message):
        if message.author.bot:
            return

        ctx = await self.get_context(message)
        if ctx.invoked_with:
            await self.invoke(ctx)
        elif (intent := await self.get_intent(message))['intent'] is not None:
            logger.debug(f'Find intent {intent}')
        else:
            await self.default_answer(message)

    async def get_intent(self, message):
        if len(message.content) < 20:
            return {
                'intent': None
            }
        await asyncio.sleep(1)
        return {
            'intent': None
        }

    async def default_answer(self, message):
        if message.channel.type == ChannelType.private:
            await message.channel.send('Я еще не умею понимать свободную речь, напиши в чате\n>help\nдля вывода документации')