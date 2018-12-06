import discord
import time
from discord.ext import commands
import logging


class Ranks:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['officer', 'cop'])
    @commands.guild_only()
    async def leo(self, ctx):
        leo = discord.utils.get(ctx.guild.roles, name="Active Officer")
        print("{} used the LEO command".format(ctx.author))
        if discord.utils.get(ctx.guild.roles, name="Active Officer"):
            if discord.utils.get(ctx.author.roles, name="Active Officer"):
                await ctx.author.remove_roles(leo, reason="LEO Command recieved.")
                await ctx.send("{}, you have signed out of active duty.".format(ctx.author))
            else:
                await ctx.author.add_roles(leo, reason="LEO command recieved.")
                await ctx.send("{}, you have logged in to active duty.".format(ctx.author))
        else:
            await ctx.send("There is no role called 'Active Officer'")

    @commands.command(aliases=['civ'])
    @commands.guild_only()
    async def civilian(self, ctx):
        civ = discord.utils.get(ctx.guild.roles, name="Active Civilian")
        print("{} used the civ command".format(ctx.author))
        if discord.utils.get(ctx.guild.roles, name="Active Civilian"):
            if discord.utils.get(ctx.author.roles, name="Active Civilian"):
                await ctx.author.remove_roles(civ, reason="Civ Command recieved.")
                await ctx.send("{}, you have signed out of LifeInvader.".format(ctx.author))
            else:
                await ctx.author.add_roles(civ, reason="Civ command recieved.")
                await ctx.send("{}, you have logged in to LifeInvader".format(ctx.author))
        else:
            await ctx.send("There is no role called 'Active Civilian'")

    @commands.command(aliases=['fire', 'medic', 'medical'])
    @commands.guild_only()
    async def ems(self, ctx):
        ems = discord.utils.get(ctx.guild.roles, name="Active EMS")
        print("{} used the ems command".format(ctx.author))
        if discord.utils.get(ctx.guild.roles, name="Active EMS"):
            if discord.utils.get(ctx.author.roles, name="Active EMS"):
                await ctx.author.remove_roles(ems, reason="EMS Command recieved.")
                await ctx.send("{}, you have signed out of active duty.".format(ctx.author))
            else:
                await ctx.author.add_roles(ems, reason="LEO command recieved.")
                await ctx.send("{}, you have logged in to active duty.".format(ctx.author))
        else:
            await ctx.send("There is no role called 'Active EMS'")

    @commands.command(aliases=['people'])
    @commands.guild_only()
    async def ratio(self, ctx):
        leo = discord.utils.get(ctx.guild.roles, name="Active Officer")
        civ = discord.utils.get(ctx.guild.roles, name="Active Civilian")
        ems = discord.utils.get(ctx.guild.roles, name="Active EMS")
        dispatch = discord.utils.get(
            ctx.guild.roles, name="Active Communicator")
        leo = leo.members
        civ = civ.members
        ems = ems.members
        dispatch = dispatch.members
        leo = len(leo)
        civ = len(civ)
        ems = len(ems)
        dispatch = len(dispatch)

        print("{} used the ratio command".format(ctx.author))

        await ctx.send("There is {0} Cops, {1} Civilians, {2} SAFD and {3} dispatchers".format(leo, civ, ems, dispatch))

    @commands.command(aliases=['rem-rank'])
    @commands.guild_only()
    async def remove_ranks(self, ctx):
        leo = discord.utils.get(ctx.guild.roles, name="Active Officer")
        leo_members = leo.members

        ems = discord.utils.get(ctx.guild.roles, name="Active EMS")
        ems_members = ems.members

        civ = discord.utils.get(ctx.guild.roles, name="Active Civilian")
        civ_members = civ.members
        print("{} used the remove_ranks command".format(ctx.author))
        if discord.utils.get(ctx.author.roles, name="Trusted Player"):
            for civmember in civ_members:
                civilian = discord.utils.get(
                    ctx.guild.members, id=civmember.id)

                await civilian.remove_roles(civ)

            for leomember in leo_members:
                officer = discord.utils.get(
                    ctx.guild.members, id=leomember.id)

                await officer.remove_roles(leo)

            for emsmember in ems_members:
                medic = discord.utils.get(
                    ctx.guild.members, id=emsmember.id)

                await medic.remove_roles(ems)

            await ctx.send("All active roles have been removed.")
        else:
            await ctx.send("Only a trusted player can do this!")


def setup(bot):
    bot.add_cog(Ranks(bot))
