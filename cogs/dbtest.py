import discord
import time
from discord.ext import commands
import aiosqlite
import asyncio


class dbtest:
    def __init__(self, bot):
        self.bot = bot

    async def botdb(self):
        async with aiosqlite.connect('utils/bot.db') as db:
            await db.execute('''CREATE TABLE stocks
                (date text, trans text, symbol text, qty real, price real)''')
            await db.commit()

    @commands.command()
    async def dbtester(self, ctx):
        await self.botdb()
        await ctx.send("completed")


def setup(bot):
    bot.add_cog(dbtest(bot))
