from discord.ext import commands
import random


class Fun:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def coin(self, ctx):
        channel = ctx.message.channel
        toss = random.randint(0, 1)
        author = ctx.message.author
        print("{0} used the coinflip command!".format(author))
        try:
            if toss == 0:
                await channel.send("Heads!")
            else:
                await channel.send("Tails :(")

    @commands.command()
    @commands.guild_only()
    async def blame(self, ctx):
        print("{} has used the blame command".format(ctx.author))
        await ctx.send("What has Adam done now :rolling_eyes:")

    @commands.command()
    @commands.guild_only()
    async def urm(self, ctx):
        channel = ctx.message.channel
        await channel.send("Jen stop being weird, if it isn't Jen.. stop being weird.")
        print("{0} has used the URM command".format(ctx.message.author))


def setup(bot):
    bot.add_cog(Fun(bot))
