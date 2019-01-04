import discord
from discord.ext import commands
import asyncio


class Money:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def ticket(self, ctx):
        ticketRole = ctx.guild.get_role(513653523905380372)
        guildTicket = ctx.guild

        def checkOne(m):
            return m.mentions and m.author == ctx.author and m.channel == ctx.channel

        def checkTwo(m):
            return m.author == ctx.author and m.channel == ctx.channel

        await ctx.send("Who is this for? [*tag them*]")
        fineTarget = await self.bot.wait_for('message', check=checkOne)
        await asyncio.sleep(1)

        await ctx.send("How much is it? [*don't use a currency prefix*]")
        fineAmount = await self.bot.wait_for('message', check=checkTwo)
        await asyncio.sleep(1)

        await ctx.send("What is the in-game character name?")
        charName = await self.bot.wait_for('message', check=checkTwo)
        await asyncio.sleep(1)

        await ctx.send("What did the offender do?")
        fineReason = await self.bot.wait_for('message', check=checkTwo)
        await asyncio.sleep(1)

        mentionId = fineTarget.mentions[0]
        mentionMember = guildTicket.get_member(mentionId.id)

        print(repr(mentionId))

        await ctx.send("{0} has been fined ${1}".format(mentionId.mention, fineAmount.content))
        await mentionMember.add_roles(ticketRole, reason="For the fine", atomic=True)
        await mentionMember.send(
            f"Your character {charName.content} has been fined ${fineAmount.content}. To pay off this fine do `/pay (~)SADPS {fineAmount.content}` and after that do `~ticketpaid`. You got this ticket because: {fineReason.content}")

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
