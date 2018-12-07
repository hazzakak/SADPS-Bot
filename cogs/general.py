import discord
import time
from discord.ext import commands
import logging
from discord.ext.commands.cooldowns import BucketType
import traceback
import sys

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
        'command_name': '~ratio (*or ~people*)',
        'description': '`Gives you the ratio of the current amount of people!`'
    }
]

help3 = [
    {
        'command_name': '~remove_ranks **Staff Command** (*or ~rem-rank*)',
        'description': '`Removes everyones active roles!`'
    }
]


class General:
    def __init__(self, bot):
        self.bot = bot

    def is_staff(self, ctx):
        author = ctx.message.author
        if discord.utils.get(author.roles, name="Staff"):
            return True

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
        author = ctx.message.author
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
        crim = discord.utils.get(guild.roles, name="Civilian/Criminal").mention
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
        if dispatch == None:
            await channel.send("The dispatcher role doesn not exist, command cannot be excecuted.")
        else:
            await channel.send("{0} a 911 call has been initiated: {1}".format(dispatch.mention, reason))
            print("911 command used by {0}".format(ctx.message.author))


def setup(bot):
    bot.add_cog(General(bot))
