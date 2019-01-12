import discord
from discord.ext import commands
import aiosqlite
import asyncio


class General:
    def __init__(self, bot):
        self.bot = bot

    def is_staff(self, ctx):
        author = ctx.message.author
        if discord.utils.get(author.roles, name="Staff"):
            return True
        else:
            return False

    async def addSimpleCommandDB(self, simpleCommand, response):
        async with aiosqlite.connect('utils/bot.db') as db:
            await db.execute('INSERT INTO simpleCommands (command, response) VALUES ("{0}", "{1}")'.format(simpleCommand, response.capitalize()))
            await db.commit()
            return

    async def inserthelp(self, command, desc):
        async with aiosqlite.connect('utils/bot.db') as db:
            await db.execute('INSERT INTO helplist (command, description) VALUES ("{0}", "{1}")'.format(command, desc.capitalize()))
            await db.commit()
            return

    async def searchhelp(self, page):
        async with aiosqlite.connect('utils/bot.db') as db:
            offset = page*10-10
            sql = 'SELECT * FROM helplist LIMIT 10 OFFSET ?'
            cursor = await db.execute(sql, (offset,))
            return await cursor.fetchall()

    async def viewAscDB(self):
        async with aiosqlite.connect('utils/bot.db') as db:
            db.row_factory = aiosqlite.Row
            sql = 'SELECT * FROM simpleCommands'
            cursor = await db.execute(sql)

            rows = await cursor.fetchall()
            return rows
            await cursor.close()

    async def deleteAscDB(self, id):
        async with aiosqlite.connect('utils/bot.db') as db:
            sql = 'DELETE FROM simpleCommands WHERE id = ?'
            cursor = await db.execute(sql, (id,))

            await db.commit()

    @commands.cooldown(1, 1800, commands.BucketType.guild)
    @commands.command()
    @commands.guild_only()
    async def priority(self, ctx):
        channel = ctx.message.channel
        author = str(ctx.message.author)
        guild = ctx.guild
        crim = discord.utils.get(guild.roles, name="Active Civilian").mention
        if ctx.message.guild.id == 473968917468020767:
            print('Priority command used by: {0}'.format(author))
            await channel.send("{} there is a priority at the moment, please wait 30 minute until you do one!".format(crim))
        else:
            print('Priority command attempted by {0}'.format(author))
            await channel.send("This command can only be used in the main server!")

    @commands.command()
    @commands.guild_only()
    @commands.has_role("Staff")
    async def reset_priority(self, ctx):
        channel = ctx.message.channel
        self.priority.reset_cooldown(ctx)
        await channel.send("The priority cooldown has been reset, the command can be used.")
        print("Priority reset command  used by {0}".format(
            ctx.message.author))

    @commands.command(name="911")
    @commands.guild_only()
    async def nine(self, ctx, *, reason):
        channel = ctx.message.channel
        dispatch = ctx.guild.get_role(515649817998000139)
        if dispatch is None:
            await channel.send("The dispatcher role doesn't not exist, command cannot be executed.")
        else:
            await channel.send("{0} a 911 call has been initiated: {1}".format(dispatch.mention, reason))
            print("911 command used by {0}".format(ctx.message.author))

    @commands.command()
    @commands.guild_only()
    async def testing123(self, ctx):
        print(ctx.message.author.voice)
        discordget = ctx.guild.get_channel(507052685170704399)
        print(discordget)

    @commands.command()
    @commands.guild_only()
    async def suggest(self, ctx, *, suggestion):
        devServer = discord.utils.get(self.bot.guilds, id=507052685170704394)
        sugChannel = discord.utils.get(
            devServer.channels, id=522618999830478848)
        message = ":white_check_mark: your suggestion has been sent through to the development team, please wait for their verdict."
        await ctx.send(message)
        await asyncio.sleep(3)

        sugMessage = await sugChannel.send(f"**{suggestion}** by *{ctx.author.nick}*")

        await sugMessage.add_reaction("\U0001f44d")
        await sugMessage.add_reaction("\U0001f44e")

    @commands.command()
    @commands.guild_only()
    @commands.is_owner()
    async def addcommand(self, ctx):
        def checkTwo(m):
            return m.author == ctx.author and m.channel == ctx.channel

        await ctx.send("What is the command called?")
        await asyncio.sleep(1)
        command = await self.bot.wait_for('message', check=checkTwo)

        await ctx.send("What is the command description?")
        await asyncio.sleep(1)
        desc = await self.bot.wait_for('message', check=checkTwo)

        await asyncio.sleep(3)
        await self.inserthelp(command.content, desc.content)

        await ctx.send(f"The command `{command.content}` with the description `{desc.content}` has been added the the help list.")

    @commands.command(aliases=['helplist'])
    @commands.guild_only()
    async def help(self, ctx, page: int = 1):
        embed = discord.Embed(
            title='Helplist',
            colour=discord.Colour.orange()
        )
        embed.set_footer(text="Bot created by harryjoseph#3275")
        embed.set_thumbnail(url='https://i.imgur.com/LX8d1xH.jpg')
        embed.set_author(name='SADPS Bot',
                         icon_url='https://i.imgur.com/LX8d1xH.jpg')
        rows = await self.searchhelp(page)
        print(rows)
        if rows == []:
            await ctx.send("That page number does not exist.")
        else:
            for row in rows:
                embed.add_field(
                    name=f"Command: `{row[1]}`", value=f"{row[2]}", inline=False)
            await ctx.send(embed=embed)

    @commands.command(aliases=['asc', 'add-cmd', 'addcmd'])
    @commands.guild_only()
    async def addSimpleCommand(self, ctx):
        if ctx.author.id == 302454373882003456 or ctx.author.id == 424614954310565888 or ctx.author.id == 396034970788823042:
            def check(m):
                return m.author == ctx.author and m.channel == ctx.channel

            await ctx.send("What is the command?")
            await asyncio.sleep(1)
            command = await self.bot.wait_for('message', check=check)
            if command.content.strip().count(' ') > 0:
                await ctx.send("The command can only have one word.")
                return

            await ctx.send("What should it respond?")
            await asyncio.sleep(1)
            response = await self.bot.wait_for('message', check=check)

            await self.addSimpleCommandDB(command.content.lower(), response.content)

            await ctx.send(f"Command `~{command.content}` has been added with the response: `{response.content}`")
        else:
            await ctx.send("You are not permitted to create a simple command.")

    @commands.command(aliases=['simplecommands'])
    @commands.guild_only()
    async def viewAsc(self, ctx):
        embed = discord.Embed(
            title='Simple Commands',
            colour=discord.Colour.green()
        )
        embed.set_footer(text="Bot created by harryjoseph#3275")
        embed.set_thumbnail(url='https://i.imgur.com/LX8d1xH.jpg')
        embed.set_author(name='SADPS Bot',
                         icon_url='https://i.imgur.com/LX8d1xH.jpg')
        viewSimpleCommands = await self.viewAscDB()
        for command in viewSimpleCommands:
            embed.add_field(
                name=f"({command['id']}) {command['command']}", value=f"{command['response']}", inline=False)
        await ctx.send(embed=embed)

    @commands.command(aliases=['delete-asc'])
    @commands.guild_only()
    async def delAsc(self, ctx, id: int):
        if ctx.author.id == 302454373882003456 or ctx.author.id == 424614954310565888 or ctx.author.id == 396034970788823042:
            await self.deleteAscDB(id)
            await ctx.send(f"The command with ID: {id} has been deleted!")
        else:
            await ctx.send("You are not permitted to delete a simple command.")

    @commands.command()
    @commands.guild_only()
    @commands.has_any_role("Department Head", "FTO Director", "Staff", "FTO Deputy Director", "Assistant Department Head")
    async def cadets(self, ctx):
        mainServer = self.bot.get_guild(473968917468020767)
        cadetsRole = discord.utils.get(mainServer.roles, name="Needs Training")
        cadetsMembers = cadetsRole.members

        bcsoRole = discord.utils.get(
            mainServer.roles, name="Blaine County Sheriffs Office")
        lspdRole = discord.utils.get(
            mainServer.roles, name="Los Santos Police Department")
        sahpRole = discord.utils.get(
            mainServer.roles, name="San Andreas Highway Patrol")

        embedBCSO = discord.Embed(
            title="Cadet Tracker", colour=discord.Colour.green(), inline=False)
        embedBCSO.set_footer(text="Bot created by harryjoseph#3275")
        embedBCSO.set_author(name='SADPS Bot',
                             icon_url='https://i.imgur.com/LX8d1xH.jpg')

        embedLSPD = discord.Embed(
            title="Cadet Tracker", colour=discord.Colour.blue(), inline=False)
        embedLSPD.set_footer(text="Bot created by harryjoseph#3275")
        embedLSPD.set_author(name='SADPS Bot',
                             icon_url='https://i.imgur.com/LX8d1xH.jpg')

        embedSAHP = discord.Embed(
            title="Cadet Tracker", colour=discord.Colour.orange(), inline=False)
        embedSAHP.set_footer(text="Bot created by harryjoseph#3275")
        embedSAHP.set_author(name='SADPS Bot',
                             icon_url='https://i.imgur.com/LX8d1xH.jpg')

        for cadet in cadetsMembers:
            if bcsoRole in cadet.roles:
                embedBCSO.add_field(
                    name="BCSO:", value=f"`{cadet.nick}`", inline=False)

            if sahpRole in cadet.roles:
                embedSAHP.add_field(
                    name="SAHP:", value=f"`{cadet.nick}`", inline=False)

            if lspdRole in cadet.roles:
                embedLSPD.add_field(
                    name="LSPD:", value=f"`{cadet.nick}`", inline=False)
        await ctx.send(embed=embedBCSO)
        await ctx.send(embed=embedLSPD)
        await ctx.send(embed=embedSAHP)

    @commands.command()
    @commands.guild_only()
    @commands.has_any_role("Department Head", "Staff")
    async def deptcheck(self, ctx):
        mainServer = self.bot.get_guild(473968917468020767)
        cadetsRole = discord.utils.get(mainServer.roles, name="Needs Training")
        cadetsMembers = cadetsRole.members

        rideAlong1 = discord.utils.get(mainServer.roles, name="Ride Along #1")
        rideAlong2 = discord.utils.get(mainServer.roles, name="Ride Along #2")
        rideAlong3 = discord.utils.get(mainServer.roles, name="Ride Along #3")

        bcsoRole = discord.utils.get(
            mainServer.roles, name="Blaine County Sheriffs Office")
        lspdRole = discord.utils.get(
            mainServer.roles, name="Los Santos Police Department")
        sahpRole = discord.utils.get(
            mainServer.roles, name="San Andreas Highway Patrol")

        bcsoCount = len(bcsoRole.members)
        lspdCount = len(lspdRole.members)
        sahpCount = len(sahpRole.members)

        embedBCSO = discord.Embed(
            title="BCSO Information", colour=discord.Colour.green(), inline=False)
        embedBCSO.set_footer(text="Bot created by harryjoseph#3275")
        embedBCSO.set_author(name='SADPS Bot',
                             icon_url='https://i.imgur.com/LX8d1xH.jpg')

        embedLSPD = discord.Embed(
            title="LSPD Information", colour=discord.Colour.blue(), inline=False)
        embedLSPD.set_footer(text="Bot created by harryjoseph#3275")
        embedLSPD.set_author(name='SADPS Bot',
                             icon_url='https://i.imgur.com/LX8d1xH.jpg')

        embedSAHP = discord.Embed(
            title="SAHP Information", colour=discord.Colour.orange(), inline=False)
        embedSAHP.set_footer(text="Bot created by harryjoseph#3275")
        embedSAHP.set_author(name='SADPS Bot',
                             icon_url='https://i.imgur.com/LX8d1xH.jpg')

        if discord.utils.get(ctx.author.roles, name="Blaine County Sheriffs Office"):
            embedBCSO.add_field(
                name="Members:", value=f"{bcsoCount}")

            for cadet in cadetsMembers:
                if bcsoRole in cadet.roles:
                    embedBCSO.add_field(
                        name="Cadet:", value=f"**-** `{cadet.nick}`")

            for rideAlong in rideAlong1.members:
                if bcsoRole in rideAlong.roles:
                    embedBCSO.add_field(
                        name="Ride Along #1:", value=f"**-** `{rideAlong.nick}`")

            for rideAlong in rideAlong2.members:
                if bcsoRole in rideAlong.roles:
                    embedBCSO.add_field(
                        name="Ride Along #2:", value=f"**-** `{rideAlong.nick}`")

            for rideAlong in rideAlong3.members:
                if bcsoRole in rideAlong.roles:
                    embedBCSO.add_field(
                        name="Ride Along #3:", value=f"**-** `{rideAlong.nick}`")
            await ctx.send(embed=embedBCSO)

        if discord.utils.get(ctx.author.roles, name="San Andreas Highway Patrol"):
            embedSAHP.add_field(
                name="Members:", value=f"{sahpCount}")

            for cadet in cadetsMembers:
                if sahpRole in cadet.roles:
                    embedSAHP.add_field(
                        name="Cadet:", value=f"**-** `{cadet.nick}`")

            for rideAlong in rideAlong1.members:
                if sahpRole in rideAlong.roles:
                    embedSAHP.add_field(
                        name="Ride Along #1:", value=f"**-** `{rideAlong.nick}`")

            for rideAlong in rideAlong2.members:
                if sahpRole in rideAlong.roles:
                    embedSAHP.add_field(
                        name="Ride Along #2:", value=f"**-** `{rideAlong.nick}`")

            for rideAlong in rideAlong3.members:
                if sahpRole in rideAlong.roles:
                    embedSAHP.add_field(
                        name="Ride Along #3:", value=f"**-** `{rideAlong.nick}`")
            await ctx.send(embed=embedSAHP)

        if discord.utils.get(ctx.author.roles, name="Los Santos Police Department"):
            embedLSPD.add_field(
                name="Members:", value=f"{lspdCount}")

            for cadet in cadetsMembers:
                if lspdRole in cadet.roles:
                    embedLSPD.add_field(
                        name="Cadet:", value=f"**-** `{cadet.nick}`")

            for rideAlong in rideAlong1.members:
                if lspdRole in rideAlong.roles:
                    embedLSPD.add_field(
                        name="Ride Along #1:", value=f"**-** `{rideAlong.nick}`")

            for rideAlong in rideAlong2.members:
                if lspdRole in rideAlong.roles:
                    embedLSPD.add_field(
                        name="Ride Along #2:", value=f"**-** `{rideAlong.nick}`")

            for rideAlong in rideAlong3.members:
                if lspdRole in rideAlong.roles:
                    embedLSPD.add_field(
                        name="Ride Along #3:", value=f"**-** `{rideAlong.nick}`")

            await ctx.send(embed=embedLSPD)


def setup(bot):
    bot.add_cog(General(bot))
