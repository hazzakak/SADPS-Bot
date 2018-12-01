import discord
from discord.ext import commands
import asyncio


class Sounds:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def soundtest(self, ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()

    @commands.command()
    async def pager(self, ctx):
        source = discord.PCMVolumeTransformer(
            discord.FFmpegPCMAudio('/root/bot/cogs/Sounds/pager.mp3'))
        channel_text = ctx.message.channel
        author = str(ctx.message.author)
        print('Pager command used by: ' + author)
        server = ctx.message.guild
        if not ctx.message.author.voice:
            await channel_text.send('You are not in a voice channel!')
        else:
            channel = ctx.message.author.voice.channel
            vc = await channel.connect()
            vc.play(source, after=None)
            await channel_text.send('The pager sound has now been alarmed!')
            await asyncio.sleep(6)
            await vc.disconnect()

    @commands.command(aliases=['dis'])
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()


def setup(bot):
    bot.add_cog(Sounds(bot))
