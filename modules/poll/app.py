import asyncio

import discord
from discord.ext import commands

from modules.base.ext import BaseBot


class Poll:
    """
    Класс голосования с аттрибутами шаблонами
    А также методом для постройки голосования
    """
    react_list = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
    message = "Внимание! Новое голосование!\n" \
              "Варианты:"
    color = discord.Colour.from_rgb(108, 145, 191)
    result = f"По итогам голосования:\n"

    @staticmethod
    def build_msg(*options):
        """
        Метод, который на основе переданных опций собирает новое голосование
        """
        if not options:
            new_message = Poll.message + "\n✅ = __*Да*__" \
                                         "\n❎ = __*Нет*__"
            return new_message
        else:
            new_message = Poll.message
            for ind, option in enumerate(options):
                new_message += f"\n{ind + 1}) __*{option}*__"
            return new_message


class PollBot(BaseBot):
    """
    Набор функций для проведения голосования
    Как использовать:
    >poll "Тема"(в кавычках) %время в секундах до подсчёта% "n-ое кол-во вариантов ответа(максимум 10)"
    Пример:
    >poll "Провести сегодня пару?" 60 Да Нет "На ваше усмотрение"
    Если нету вариантов ответа, то по умолчанию ставиться Да/Нет.
    """
    __name__ = 'Голосование'


    @commands.command(name="poll",
                      pass_context=True)
    async def execute(self, ctx, question, time: int, *options):
        """
        Начало голосования. Пример >poll "вопрос" время_на_сбор_ответов [вариант_ответа_1 вариант_ответа_2]
        """

        message = Poll.build_msg(*options)
        react_message = await self.send_msg(ctx, question, message)

        await self.add_react(react_message, *options)
        await asyncio.sleep(time)
        await self.send_result(ctx, react_message, *options)

    @execute.error
    async def errors(self, ctx, error):
        await ctx.send('Вы не правильно ввели команду.\nПопробуйте так: >poll "Вопрос?" 60 "Да" "Нет" "На ваше усмотрение"')

    async def send_msg(self, ctx, question, message):
        embed = discord.Embed(title=question, color=Poll.color, description=message)
        react_message = await ctx.send(embed=embed)

        return react_message

    async def add_react(self, message, *options):
        if not options:
            await message.add_reaction('✅')
            await message.add_reaction('❎')
        else:
            for i in range(len(options)):
                await message.add_reaction(Poll.react_list[i])

    async def send_result(self, ctx, message, *options):
        channel = message.channel
        message = await channel.fetch_message(message.id)
        result = Poll.result

        if not options:
            result += f"\nКол-во ✅ = {message.reactions[0].count - 1}" \
                      f"\nКол-во ❎ = {message.reactions[1].count - 1}"
        else:
            for i in range(len(options)):
                result += f"\nКол-во {Poll.react_list[i]} = {message.reactions[i].count - 1}"

        await ctx.reply(result)