import discord
from discord.ext import commands
import aiosqlite
import asyncio

help1 = [
    {
        'command_name': '~rpstart',
        'description': '`Notifies SADPS that there is an RP starting!`'
    },
    {
        'command_name': '~rpover',
        'description': '`Notifies SADPS that the RP is ending.` :('
    }, {
        'command_name': '~rpjoin',
        'description': "`Notifies SADPS that there is an RP and it needs people!`"
    }, {
        'command_name': '~echo  <content> **Staff Command**',
        'description': '`Says RP is live, come and join`'
    }, {
        'command_name': '~ping',
        'description': '`Tests the functionality of the bot with a simple, Ping Pong command.`'
    }, {
        'command_name': '~clear (default=1) <amount> **Staff Command**',
        'description': '`Clears the amount of messages you specified!`'
    }, {
        'command_name': '~pager',
        'description': '`Sounds the pager alarm!`'
    }, {
        'command_name': '~priority',
        'description': '`Begin priority timer (30 minutes).`'
    }, {
        'command_name': '~reset_priority **Staff Command**',
        'description': '`Resets the priority timer, ONLY TO BE USED BY STAFF`'
    }
]

help2 = [
    {
        'command_name': '~ticket <amount> <offender tag> <character name>',
        'description': '`This gives the person a ticket.`'
    }, {
        'command_name': '~ticketpaid',
        'description': '`This removes the ticket (after being paid)`'
    }, {
        'command_name': '~911 <reason>',
        'description': '`Be a snitch and call 911`'
    }, {
        'command_name': '~coin',
        'description': '`Heads or tails!`'
    }, {
        'command_name': '~leo (*or ~cop, ~officer*)',
        'description': '`Gives or removes the Active Officer role.`'
    }, {
        'command_name': '~ems (*or ~medic, ~fire, ~medical*)',
        'description': '`Gives or removes the Active EMS role.`'
    }, {
        'command_name': '~civ (*or ~civilian*)',
        'description': '`Gives or removes the Active Civilian role.`'
    }, {
        'command_name': '~dispatch (*or ~dispatcher, ~disp, ~comms, ~communications*)',
        'description': '`Gives or removes the Active Communicator role.`'
    }
]

help3 = [
    {
        'command_name': '~remove_ranks **Trusted Player Command** (*or ~rem-rank*)',
        'description': '`Removes everyones active roles!`'
    }, {
        'command_name': '~ratio (*or ~people*)',
        'description': '`Gives you the ratio of the current amount of people!`'
    }
]


class General:
    def __init__(self, bot):
        self.bot = bot

    def is_staff(self, ctx):
        author = ctx.message.author
        if discord.utils.get(author.roles, name="Staff"):
            return True
        else:
            return False

    @commands.command(pass_context=True)
    @commands.guild_only()
    async def rpstart(self, ctx):
        disabled = False
        channel = ctx.message.channel
        print('RPStart command used by: ' + str(ctx.message.author))
        if disabled is False:
            await channel.send("@everyone rp is starting join RP staging!")
        else:
            await channel.send("This command is disabled :open_mouth:")

    @commands.command(pass_context=True)
    @commands.guild_only()
    async def rpover(self, ctx):
        channel = ctx.message.channel
        author = str(ctx.message.author)
        print('RPOver command used by: {}'.format(author))
        disabled = False
        if disabled is False:
            await channel.send("@here Rp over leave your roles before Luis catches you.")
        else:
            await channel.send("This command is disabled :open_mouth:")

    @commands.command(pass_context=True)
    @commands.guild_only()
    async def rpjoin(self, ctx):
        channel = ctx.message.channel
        author = str(ctx.message.author)
        print('RPOver command used by: {}'.format(author))
        disabled = False
        if disabled is False:
            await channel.send("RP is live, come and join, @everyone")
        else:
            await channel.send("This command is disabled :open_mouth:")

    @commands.command(pass_context=True)
    @commands.guild_only()
    async def help(self, ctx, page: int = 1):
        author = str(ctx.message.author)
        channel = ctx.message.channel
        print('Help command used by: ' + author)
        embed = discord.Embed(
            title='Help',
            colour=discord.Colour.blue()
        )
        embed.set_footer(text="Bot created by harryjoseph#3275")
        embed.set_thumbnail(url='https://i.imgur.com/LX8d1xH.jpg')
        embed.set_author(name='SADPS Bot',
                         icon_url='https://i.imgur.com/LX8d1xH.jpg')
        print('{}'.format(page))
        if page == 1:
            for command in help1:
                embed.add_field(
                    name=command['command_name'], value=command['description'], inline=False)
            embed.add_field(
                name="~help 2", value="for the next page", inline=False)
            await ctx.author.send(embed=embed)
            await channel.send('You have been private messaged the help list!')
        elif page == 2:
            for command in help2:
                embed.add_field(
                    name=command['command_name'], value=command['description'], inline=False)
            embed.add_field(
                name="~help 3", value="for the next page", inline=False)
            await ctx.author.send(embed=embed)
            await channel.send('You have been private messaged the help list.')
        elif page == 3:
            for command in help3:
                embed.add_field(
                    name=command['command_name'], value=command['description'], inline=False)
            embed.add_field(
                name="Last page", value="Last page of the help list", inline=False)
            await ctx.author.send(embed=embed)
            await channel.send('You have been private messaged the help list.')
        elif page > 3:
            await ctx.send("There isn't a page {}.".format(page))

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
    async def reset_priority(self, ctx):
        channel = ctx.message.channel
        if discord.utils.get(ctx.author.roles, name="Staff"):
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
    async def suggest(self, ctx, *, suggestion):
        devServer = discord.utils.get(self.bot.guilds, id=507052685170704394)
        sugChannel = discord.utils.get(
            devServer.channels, id=522618999830478848)
        message = ":white_check_mark: Thanks for suggesting! Your suggestion has been sent through the voting process and the verdict will be verified within 24-72 hours."
        await ctx.send(message)
        await asyncio.sleep(3)

        sugMessage = await sugChannel.send(f"**{suggestion}** by *{ctx.author.nick}*")

        await sugMessage.add_reaction("\U0001f44d")
        await sugMessage.add_reaction("\U0001f44e")

    '''async def inserthelp(self, command, desc, cat):
        async with aiosqlite.connect('utils/bot.db') as db:
            await db.execute('INSERT INTO helplist (command, description, category) VALUES ("{0}", "{1}", "{2}")'.format(command, desc.capitalize(), cat.capitalize()))
            await db.commit()
            return'''

    '''@commands.command()
    @commands.guild_only()
    async def addcommand(self, ctx):
        if ctx.author.id == 302454373882003456:
            await ctx.send("What is the command called?")
            await asyncio.sleep(1)
            command = await self.bot.wait_for('message')

            await ctx.send("What is the command description?")
            await asyncio.sleep(1)
            desc = await self.bot.wait_for('message')

            await ctx.send("What is the command category?")
            await asyncio.sleep(1)
            cat = await self.bot.wait_for('message')

            await asyncio.sleep(3)
            await self.inserthelp(command.content, desc.content, cat.content)

            await ctx.send(f"The command `{command.content}` with the description `{desc.content}` has been added the the help list.")
        else:
            await ctx.send("You are not the ALMIGHTY HARRY")'''

    '''@commands.command()
    @commands.guild_only()
    async def helplist(self, ctx, category=None):
        category = category.toLowerCase()
        if category == None:
            embed = discord.Embed(
                title='Which category?',
                colour=discord.Colour.blue()
            )
            embed.set_footer(text="Bot created by harryjoseph#3275")
            embed.set_thumbnail(url='https://i.imgur.com/LX8d1xH.jpg')
            embed.set_author(name='SADPS Bot',
                             icon_url='https://i.imgur.com/LX8d1xH.jpg')
            embed.add_field(name="`General`", value=None, inline=False)
            embed.add_field(name="`Roleplay`", value=None, inline=False)
            embed.add_field(name="`Misc`", value=None, inline=False)
            embed.add_field(name="`Moderation`", value=None, inline=False)
            await ctx.send(embed=embed)
        elif category == "general":'''


def setup(bot):
    bot.add_cog(General(bot))
