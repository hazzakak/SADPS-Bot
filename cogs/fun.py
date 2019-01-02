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


def setup(bot):
    bot.add_cog(Fun(bot))
