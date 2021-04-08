from discord import member
from discord.abc import PrivateChannel
from discord.channel import ChannelType
from discord.ext.commands.context import Context
from discord.ext.commands.core import group
from loguru import logger
import aiofiles
import discord
from discord.ext import commands
from pony.utils.utils import count
from modules.base.ext import BaseBot
import re
from .models import Penalty, orm

class RaitingBot(BaseBot):
    """
    Это пример бота. Он умеет ходить домой
    Если вам нужен более продвинутый пример посмотрите модуль rules
    """
    @commands.group(name='pen')
    async def group_pen(self, ctx: Context):
        pass

    @group_pen.command(name='add')
    async def pen_add(self, ctx: Context,  obj: str, 
                    obj_type: Penalty.OBJ_TYPE = Penalty.OBJ_TYPE.STUD, msg: str = None):
        
        # ОБЯЗАТЕЛЬНО! Создание сесии с базой
        # в этом блоке СТРОГО ЗАПРЕЩЕННЫ все асинхронные операции и конструкции
        # этот блок сам делает операцию commit или rollback
        with orm.db_session:
            new_pen = Penalty(
                target=obj.lower().strip(),
                target_type=str(obj_type.value).lower().strip(),
                msg=msg,
                author=str(ctx.author.id)
            )

            # так выглядит пример запроса к БД, обратите внимание что разрешены только простые питонячии типы данных
            # все сложные типы должны бать приведенные к простым
            # обратите внимание что ponyORM использует AST дерево на основе вашего кода для генерации SQL запросов, поэтому в запросах не стоит придумывать извращений
            # так же обратите внимание на функцию count(p) это групповая функция и ponyORM автоматически напишет нужный групповой запрос
            # подробнее по генерации запросов смотрите в документации. Так же в режиме отладки все ваши запросы будут писаться в консоле на языке SQL
            q = orm.select((p.target, p.target_type, count(p)) for p in Penalty 
            # операция .first() возвращает первый элимент или None
                        if p.target == obj and p.target_type == str(obj_type.value)).first()
        # как можно видеть асинхронный код находится вне блока сессии с базой
        await ctx.author.send(f'Новый штраф добавлен{q[0]} имеет {q[2]} штрафов')

    @group_pen.command(name='list')
    async def cmd_pen_me(self, ctx: Context, target: str = None):
        if ctx.channel.type == ChannelType.private:
            with orm.db_session:
                q = orm.select(q for q in Penalty
                # обратите внимание что тут сложный тип (Penalty.OBJ_TYPE.STUD) приводится к простому
                            if q.target_type == Penalty.OBJ_TYPE.STUD.value
                            and q.target == ctx.author.display_name
                # [:] - это хак для выполнения запроса к бд, дословно можно понять так
                # извлеки все из запроса. В документации питона описан немного по другому, но смысл тот же
                )[:]
            if not q:
                await ctx.send('У вас нет штрафов')
            else:
                l = '\n'.join([(await self.bot.fetch_user(x.author)).display_name for x in q])
                await ctx.send(f'У вас {len(q)} штрафов\n{l}')
        elif any(r.name.lower() == 'admin' for r in ctx.author.roles):
            with orm.db_session:
                res = orm.select((count(p),) for p in Penalty 
                    if p.target == target and p.target_type == str(Penalty.OBJ_TYPE.STUD.value)).first()
            await ctx.message.delete()
            if res:
                await ctx.author.send(f'У {target} {res} штрафов')
            else:
                await ctx.author.send(f'У {target} нет штрафов')

