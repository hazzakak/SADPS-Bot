import discord
import time
from discord.ext import commands
import logging


class Testing:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="testing_roles")
    async def testingroles(self, ctx):
        author = ctx.message.author.roles
        print(author)

    @commands.command()
    async def testingrole(self, ctx):
        print(str(ctx.guild.get_role(473984304993796116)))


def setup(bot):
    bot.add_cog(Testing(bot))
