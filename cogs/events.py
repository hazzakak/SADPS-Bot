import discord
import time
from discord.ext import commands
import logging


class Events:
    def __init__(self, bot):
        self.bot = bot

    def sadps_server(self, member):
        return member.guild.id

    async def on_member_join(self, member):
        if member.guild.id == 473977440603996164:
            time.sleep(2)
            print(str(member) + ' has been messaged')
            await member.send('Hello there! Be sure to head of to the general chat if you have any questions, to apply go to #apply-here and and follow the instructions. Applications should take from 1-48 hours so please be patient!')
            # await member.send('Hello there! Be sure to head of to the general chat if you have any questions, to apply go to #apply-here and and follow the instructions. Applications should take from 1-48 hours so please be patient!')

    async def on_message(self, message):
        if message.guild is None:
            if not message.author.bot:
                print('{0} has messaged SADPS Bot'.format(message.author))
                await message.author.send('Hello there!')
        else:
            pass


def setup(bot):
    bot.add_cog(Events(bot))
