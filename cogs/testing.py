import discord
import time
from discord.ext import commands
import logging


class Testing:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="testing_roles")
    async def testingroles(self, ctx):
        author = ctx.message.author.roles
        print(author)

    @commands.command()
    async def testingrole(self, ctx):
        print(str(ctx.guild.get_role(473984304993796116)))

    @commands.command()
    async def testingidk(self, ctx):
        leo = discord.utils.get(ctx.guild.roles, name="Active Officer")
        civ = discord.utils.get(ctx.guild.roles, name="Active Civilian")
        ems = discord.utils.get(ctx.guild.roles, name="Active EMS")
        dispatch = discord.utils.get(
            ctx.guild.roles, name="Active Communicator")
        leo = leo.members
        civ = civ.members
        ems = ems.members
        dispatch = dispatch.members
        leo1 = len(leo)
        civ1 = len(civ)
        ems1 = len(ems)
        dispatch1 = len(dispatch)
        embed = discord.Embed(
            title='Ratio',
            colour=discord.Colour.red()
        )
        embed.set_footer(text="Bot created by harryjoseph#3275")
        embed.set_thumbnail(url='https://i.imgur.com/LX8d1xH.jpg')
        embed.set_author(name='SADPS Bot',
                         icon_url='https://i.imgur.com/LX8d1xH.jpg')
        embed.add_field(name="Yeah ok", value=leo)
        for leomember in leo:
            name = leomember.name
            embed.add_field(name="-", value="- " + name)
        await ctx.author.send(embed=embed)

    @commands.command(aliases=['lol'])
    @commands.guild_only()
    async def loool(self, ctx):
        leo = discord.utils.get(ctx.guild.roles, name="Active Officer")
        civ = discord.utils.get(ctx.guild.roles, name="Active Civilian")
        ems = discord.utils.get(ctx.guild.roles, name="Active EMS")
        dispatch = discord.utils.get(
            ctx.guild.roles, name="Active Communicator")
        leo = leo.members
        civ = civ.members
        ems = ems.members
        dispatch = dispatch.members
        leo1 = len(leo)
        civ1 = len(civ)
        ems1 = len(ems)
        dispatch1 = len(dispatch)

        # LEO Embed
        embedleo = discord.Embed(
            title="Law Enforcement", colour=discord.Colour.blue(), inline=False)
        embedleo.set_footer(text="Bot created by harryjoseph#3275")
        embedleo.set_thumbnail(url='https://i.imgur.com/LX8d1xH.jpg')
        embedleo.set_author(name='SADPS Bot',
                            icon_url='https://i.imgur.com/LX8d1xH.jpg')

        # Civ Embed
        embedciv = discord.Embed(
            title="Civilian", colour=discord.Colour.magenta(), inline=False)
        embedciv.set_footer(text="Bot created by harryjoseph#3275")
        embedciv.set_thumbnail(url='https://i.imgur.com/LX8d1xH.jpg')
        embedciv.set_author(name='SADPS Bot',
                            icon_url='https://i.imgur.com/LX8d1xH.jpg')

        # EMS Embed
        embedems = discord.Embed(
            title="EMS", colour=discord.Colour.red(), inline=False)
        embedems.set_footer(text="Bot created by harryjoseph#3275")
        embedems.set_thumbnail(url='https://i.imgur.com/LX8d1xH.jpg')
        embedems.set_author(name='SADPS Bot',
                            icon_url='https://i.imgur.com/LX8d1xH.jpg')

        # Dispatcher Embed
        embeddis = discord.Embed(
            title="Dispatcher", colour=discord.Colour.green(), inline=False)
        embeddis.set_footer(text="Bot created by harryjoseph#3275")
        embeddis.set_thumbnail(url='https://i.imgur.com/LX8d1xH.jpg')
        embeddis.set_author(name='SADPS Bot',
                            icon_url='https://i.imgur.com/LX8d1xH.jpg')

        if discord.utils.get(ctx.guild.roles, name="Trusted Player"):
            for leomember in leo:
                name = leomember.name
                embedleo.add_field(name="[Officer]", value=name, inline=False)

            for civmember in civ:
                name = civmember.name
                embedciv.add_field(name="[Civilian]", value=name, inline=False)

            for emsmember in ems:
                name = emsmember.name
                embedems.add_field(name="[SAFD]", value=name, inline=False)

            for dismember in dispatch:
                name = dismember.name
                embeddis.add_field(
                    name="[Dispatcher]", value=name, inline=False)

            await ctx.author.send(embed=[embedciv, embeddis])

        print("{} used the ratio command".format(ctx.author))

        await ctx.send("There is {0} Cops, {1} Civilians, {2} SAFD and {3} dispatchers".format(leo1, civ1, ems1, dispatch1))


def setup(bot):
    bot.add_cog(Testing(bot))
