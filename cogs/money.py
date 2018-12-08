import discord
from discord.ext import commands


class Money:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def ticket(self, ctx, fineAmount, fineTarget: discord.Member, *, characterName):
        channel = ctx.message.channel
        role = ctx.guild.get_role(513653523905380372)
        print("{0} has been given a ticket.".format(fineTarget))
        await channel.send("{0} has been fined ${1}".format(fineTarget, fineAmount))
        await fineTarget.add_roles(role, reason="For the fine", atomic=True)
        await fineTarget.send(
            f"Your character {characterName} has been fined ${fineAmount}. To pay off this fine do `/ pay(~)SADPS"
            " {fineAmount}` and after that do `~ticketpaid`.")

    @commands.command()
    @commands.guild_only()
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


def setup(bot):
    bot.add_cog(Money(bot))
