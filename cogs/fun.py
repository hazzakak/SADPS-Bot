import discord
import time
from discord.ext import commands
import logging
import random


class Fun:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def coin(self, ctx):
        channel = ctx.message.channel
        toss = random.randint(0, 1)
        author = ctx.message.author
        print("{0} used the coinflip command!".format(author))
        if toss == 0:
            await channel.send("Heads!")
        else:
            await channel.send("Tails :(")

    @commands.command()
    async def blame(self, ctx):
        print("{} has used the blame command".format(ctx.author))
        await ctx.send("What has Adam done now :rolling_eyes:")


def setup(bot):
    bot.add_cog(Fun(bot))
