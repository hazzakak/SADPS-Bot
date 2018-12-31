import asyncio
import discord
from discord.ext import commands


class Sounds:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def soundtest(self, ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()

    @commands.command()
    @commands.guild_only()
    async def pager(self, ctx):
        source = discord.PCMVolumeTransformer(
            discord.FFmpegPCMAudio('/root/bot/cogs/Sounds/pager.mp3'))
        channel_text = ctx.message.channel
        author = str(ctx.message.author)
        print('Pager command used by: ' + author)
        if not ctx.message.author.voice:
            await channel_text.send('You are not in a voice channel!')
        elif ctx.author.voice.channel == ctx.guild.get_channel(474393417590243329):
            channel = ctx.message.author.voice.channel
            vc = await channel.connect()
            vc.play(source, after=None)
            await channel_text.send('The pager sound has now been alarmed!')
            await asyncio.sleep(6)
            await vc.disconnect()
        else:
            await ctx.send("You cannot play the pager sound in this channel!")

    @commands.command(aliases=['dis'])
    @commands.guild_only()
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()


def setup(bot):
    bot.add_cog(Sounds(bot))
