import discord
import time
from discord.ext import commands
import logging
import asyncpg
from datetime import datetime


class Test:
    def __init__(self, bot):
        self.bot = bot

    async def main():
        conn = await asyncpg.connect('postgresql://postgres:pass@localhost:5432/discord')
        await conn.execute('''
        CREATE TABLE users(
            id serial PRIMARY KEY,
            name text,
            dob date
            )
        ''')

        await conn.execute('''
        INSERT INTO users(name, dob) VALUES($1, $2)
        ''', 'Bob', datetime.date(1984, 3, 1))

        await conn.close()

    asyncio.get_event_loop().run_until_complete(main())


def setup(bot):
    bot.add_cog(Test(bot))
