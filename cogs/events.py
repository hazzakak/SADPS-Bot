import discord
import time
import sys
import traceback
from discord.ext import commands
import aiosqlite
import asyncio


class Events:
    def __init__(self, bot):
        self.bot = bot

    async def viewSimpleCommand(self, commandName):
        async with aiosqlite.connect('utils/bot.db') as db:
            db.row_factory = aiosqlite.Row
            sql = 'SELECT * FROM simpleCommands WHERE command = ?'
            cursor = await db.execute(sql, (commandName,))

            row = await cursor.fetchone()
            return row
            await db.close()

    async def on_member_join(self, member):
        if member.guild.id == 473977440603996164:
            time.sleep(2)
            print(str(member) + ' has been messaged')
            newRole = discord.utils.get(member.guild.roles, name="Applicant")
            await member.add_roles(newRole, reason="New member")
            await member.send('Hello there! Be sure to head of to the general chat if you have any questions, to apply go to #apply-here and and follow the instructions. Applications should take from 1-48 hours so please be patient!')

    async def on_message(self, message):
        if message.guild is None:
            if not message.author.bot:
                print('{0} has messaged SADPS Bot'.format(message.author))
                await message.author.send('Hello there!')
        else:
            pass

    async def on_command_error(self, ctx, error):
        error = getattr(error, 'original', error)
        harry = discord.utils.get(ctx.guild.members, id=302454373882003456)
        commandUsed = ctx.invoked_with.lower()
        findCommand = await self.viewSimpleCommand(commandUsed)
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            await ctx.send(":x: A required argument is missing.")
        elif isinstance(error, commands.CommandOnCooldown):
            timeLeftSec = error.retry_after
            timeLeftMin = timeLeftSec / 60
            timeLeftFloat = round(timeLeftMin, 0)
            timeLeft = int(timeLeftFloat)

            print(timeLeft)

            return await ctx.send(
                f"You can not do a priority for another {timeLeft} minutes!")
        elif isinstance(error, discord.ext.commands.CommandNotFound):
            if findCommand != None:
                await ctx.send(findCommand["response"])
            else:
                await ctx.send("The command `{}` does not exist, use ~help if you're having trouble with any commands.".format(ctx.invoked_with))
        elif isinstance(error, discord.ext.commands.errors.CheckFailure):
            await ctx.send(":x: You do not have permission for this command!")
        else:
            await ctx.send("Oops, an error has occurred.")
            await harry.send(
                "An error occurred with the command: `{}` when being used by `{}`".format(ctx.command, ctx.author))
            print('Ignoring exception in command {}:'.format(
                ctx.command), file=sys.stderr)
            traceback.print_exception(
                type(error), error, error.__traceback__, file=sys.stderr)


def setup(bot):
    bot.add_cog(Events(bot))
