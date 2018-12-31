import asyncio
import logging
from datetime import datetime

import discord
from discord.ext import commands
import config as cfg


now = datetime.now().strftime("%Y-%m-%d+%H-%M")
log_name = f'logs/discord({now}).log'

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(
    filename=log_name, encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter(
    '%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

extensions = ['moderate', 'events', 'general',
              'sounds', 'money', 'testing', 'fun', 'ranks', 'dbtest']

token = cfg.token
client = commands.Bot(command_prefix="~", case_insensitive=True)
client.remove_command('help')
players = {}


@client.event
async def on_ready():
    print('Bot is online!')
    await client.change_presence(activity=discord.Game(name='SADPS | GTA V RP'))


@client.command()
async def testing(ctx):
    author = ctx.message.authorl.roles
    print(author)


@client.command()
async def load(ctx, extension):
    channel = ctx.message.channel
    if ctx.message.author.id == 302454373882003456:
        try:
            client.load_extension('cogs.' + extension)
            print('Loaded ' + extension)
            await channel.send('Loaded: ' + extension)
        except Exception as error:
            print(extension + ' cannot be loaded [' + error + ']')
            await channel.send('ERROR: Check console!')
    else:
        print('Load command attempted by:' + ctx.message.author)
        await channel.send("You're not harry?")


@client.command()
async def unload(ctx, extension):
    channel = ctx.message.channel
    if ctx.message.author.id == 302454373882003456:
        try:
            client.unload_extension('cogs.' + extension)
            print('Unloaded ' + extension)
            await channel.send('Unloaded: ' + extension)
        except Exception as error:
            print(extension + ' cannot be unloaded [' + error + ']')
            await channel.send('ERROR: Check console!')
    else:
        print('Load command attempted by:' + ctx.message.author)
        await channel.send("You're not harry?")


@client.command()
async def reload(ctx, extension):
    channel = ctx.message.channel
    if ctx.author.id == 302454373882003456:
        try:
            client.unload_extension('cogs.' + extension)
            await asyncio.sleep(1.0)
            client.load_extension('cogs.' + extension)
            await ctx.send("Reloaded: {}".format(extension))
        except Exception as error:
            print(extension + ' cannot be unloaded [' + error + ']')
            await channel.send('ERROR: Check console!')
    else:
        print('Load command attempted by:' + ctx.message.author)
        await channel.send("You're not harry?")


if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension('cogs.' + extension)
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension, error))
    client.run(token)
