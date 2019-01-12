import discord
from discord.ext import commands


class Ranks:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['officer', 'cop'])
    @commands.guild_only()
    async def leo(self, ctx):
        leo = discord.utils.get(ctx.guild.roles, name="Active Officer")
        print("{} used the LEO command".format(ctx.author))
        # Check if the server has role active {}
        if discord.utils.get(ctx.guild.roles, name="Active Officer"):
            if discord.utils.get(ctx.author.roles, name="Active Officer"):
                await ctx.author.remove_roles(leo, reason="LEO Command received.")
                await ctx.send("{}, you have signed out of active duty.".format(ctx.author))
            else:
                await ctx.author.add_roles(leo, reason="LEO command received.")
                await ctx.send("{}, you have logged in to active duty.".format(ctx.author))
        else:
            await ctx.send("There is no role called 'Active Officer'")

    @commands.command(aliases=['comms', 'communication', 'communications', 'disp', 'dispatcher'])
    @commands.guild_only()
    async def dispatch(self, ctx):
        dispatch = discord.utils.get(
            ctx.guild.roles, name="Active Communicator")
        print("{} used the comms command".format(ctx.author))
        # Check if the server has role active {}
        if discord.utils.get(ctx.guild.roles, name="Active Communicator"):
            # If user has role 'active communicator' remove it.
            if discord.utils.get(ctx.author.roles, name="Active Communicator"):
                await ctx.author.remove_roles(dispatch, reason="Comms Command received.")
                await ctx.send("{}, you have signed out of dispatch.".format(ctx.author))
            else:
                await ctx.author.add_roles(dispatch, reason="Comms command received.")
                await ctx.send("{}, you have logged in to dispatch.".format(ctx.author))
        else:
            await ctx.send("There is no role called 'Active Officer'")

    @commands.command(aliases=['civ'])
    @commands.guild_only()
    async def civilian(self, ctx):
        civ = discord.utils.get(ctx.guild.roles, name="Active Civilian")
        print("{} used the civ command".format(ctx.author))
        # Check if the server has role active {}
        if discord.utils.get(ctx.guild.roles, name="Active Civilian"):
            if discord.utils.get(ctx.author.roles, name="Active Civilian"):
                await ctx.author.remove_roles(civ, reason="Civ Command received.")
                await ctx.send("{}, you have signed out of LifeInvader.".format(ctx.author))
            else:
                await ctx.author.add_roles(civ, reason="Civ command received.")
                await ctx.send("{}, you have logged in to LifeInvader".format(ctx.author))
        else:
            await ctx.send("There is no role called 'Active Civilian'")

    @commands.command(aliases=['fire', 'medic', 'medical'])
    @commands.guild_only()
    async def ems(self, ctx):
        ems = discord.utils.get(ctx.guild.roles, name="Active EMS")
        print("{} used the ems command".format(ctx.author))
        # Check if the server has role active {}
        if discord.utils.get(ctx.guild.roles, name="Active EMS"):
            if discord.utils.get(ctx.author.roles, name="Active EMS"):
                await ctx.author.remove_roles(ems, reason="EMS Command received.")
                await ctx.send("{}, you have signed out of active duty.".format(ctx.author))
            else:
                await ctx.author.add_roles(ems, reason="LEO command received.")
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
                name = leomember.nick
                embedleo.add_field(
                    name="[Officer]", value=name, inline=False)

            for civmember in civ:
                name = civmember.nick
                embedciv.add_field(name="[Civilian]",
                                   value=name, inline=False)

            for emsmember in ems:
                name = emsmember.nick
                embedems.add_field(
                    name="[SAFD]", value=name, inline=False)

            for dismember in dispatch:
                name = dismember.nick
                embeddis.add_field(
                    name="[Dispatcher]", value=name, inline=False)

            await ctx.author.send(embed=embedleo)
            await ctx.author.send(embed=embeddis)
            await ctx.author.send(embed=embedciv)
            await ctx.author.send(embed=embedems)

        print("{} used the ratio command".format(ctx.author))

        await ctx.send("There is {0} Cops, {1} Civilians, {2} SAFD and {3} dispatchers".format(leo1, civ1, ems1, dispatch1))

    @commands.command(aliases=['rem-rank', 'remove', 'endrp'])
    @commands.guild_only()
<<<<<<< Updated upstream
    async def remove_ranks(self, ctx):
=======
    @commands.has_any_role("Staff", "Trusted Player")
    async def remove_ranks(self, ctx, user: discord.Member = None):
>>>>>>> Stashed changes
        leo = discord.utils.get(ctx.guild.roles, name="Active Officer")
        leo_members = leo.members

        ems = discord.utils.get(ctx.guild.roles, name="Active EMS")
        ems_members = ems.members

        civ = discord.utils.get(ctx.guild.roles, name="Active Civilian")
        civ_members = civ.members
        print("{} used the remove_ranks command".format(ctx.author))
<<<<<<< Updated upstream
        if discord.utils.get(ctx.author.roles, name="Trusted Player"):
=======
        if user == None:
>>>>>>> Stashed changes
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

<<<<<<< Updated upstream
=======
            for dispatchmember in dispatch_members:
                dispatcher = discord.utils.get(
                    ctx.guild.members, id=dispatchmember.id)

                await dispatcher.remove_roles(dispatch)

>>>>>>> Stashed changes
            await ctx.send("All active roles have been removed.")
        else:
            if discord.utils.get(user.roles, name="Active Officer"):
                await user.remove_roles(leo, reason=None, atomic=True)
                await ctx.send("User's role has been removed.")
            elif discord.utils.get(user.roles, name="Active Civilian"):
                await user.remove_roles(civ, reason=None, atomic=True)
                await ctx.send("User's role has been removed.")
            elif discord.utils.get(user.roles, name="Active EMS"):
                await user.remove_roles(ems, reason=None, atomic=True)
                await ctx.send("User's role has been removed.")
            elif discord.utils.get(user.roles, name="Active Communicator"):
                await user.remove_roles(dispatch, reason=None, atomic=True)
                await ctx.send("User's role has been removed.")
            else:
                await ctx.send("User does not have any active roles.")


def setup(bot):
    bot.add_cog(Ranks(bot))
