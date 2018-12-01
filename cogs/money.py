import discord
import time
import traceback
import sys
from discord.ext import commands
import logging


class Money:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ticket(self, ctx, fineAmount, fineTarget: discord.Member, *, characterName):
        channel = ctx.message.channel
        role = ctx.guild.get_role(513653523905380372)
        print("{0} has been given a ticket.".format(fineTarget))
        await channel.send("{0} has been fined ${1}".format(fineTarget, fineAmount))
        await fineTarget.add_roles(role, reason="For the fine", atomic=True)
        await fineTarget.send("Your character {0} has been fined ${1}. To pay off this fine do `/ pay(~)SADPS {1}` and after that do `~ticketpaid`.".format(characterName, fineAmount))

    @commands.command()
    async def ticketpaid(self, ctx):
        channel = ctx.message.channel
        offender = ctx.message.author
        role = ctx.guild.get_role(513653523905380372)
        if discord.utils.get(offender.roles, id=513653523905380372):
            await offender.remove_roles(role, reason="For the fine", atomic=True)
            await channel.send("Your fine has been paid.")
            print("{0} paid their ticket.".format(offender))
        else:
            await channel.send("You don't have a ticket!")
            print("{0} attempted to pay a nonexistent ticket.".format(offender))

    async def on_command_error(self, ctx, error):
        channel = ctx.message.channel
        error = getattr(error, 'original', error)
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            await ctx.send(":x: A required argument is missing.")
        elif isinstance(error, commands.CommandOnCooldown):
            return await ctx.send("You can not do more than one priority in 30 minutes!")
        else:
            print('Ignoring exception in command {}:'.format(
                ctx.command), file=sys.stderr)
            traceback.print_exception(
                type(error), error, error.__traceback__, file=sys.stderr)


def setup(bot):
    bot.add_cog(Money(bot))
