import discord
from datetime import datetime
from discord.ext import commands
import aiosqlite
import asyncio


class Moderate:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.guild_only()
    async def clear(self, ctx, amount=2):
        channel = ctx.message.channel
        messages = []
        print('Clear command used by: ' + str(ctx.message.author))
        author = ctx.message.author
        if discord.utils.get(author.roles, name="Staff"):
            async for message in channel.history(limit=int(amount)):
                messages.append(message)
            await channel.delete_messages(messages)
            await channel.send(str(amount) + ' message(s) have been deleted.')
        else:
            await channel.send('You do not have permission to use this command.')

    @commands.command(pass_context=True)
    @commands.guild_only()
    async def ping(self, ctx):
        channel = ctx.message.channel
        print('Ping command used by: ' + str(ctx.message.author))
        embed = discord.Embed(
            title='Ping',
            description="Yep, it works Adam hasn't broken it yet",
            colour=discord.Colour.blue()
        )
        embed.set_footer(text="Bot created by harryjoseph#3275")
        embed.set_thumbnail(url='https://i.imgur.com/LX8d1xH.jpg')
        embed.set_author(name='SADPS Bot',
                         icon_url='https://i.imgur.com/LX8d1xH.jpg')
        await channel.send(embed=embed)

    @commands.command(pass_context=True)
    @commands.guild_only()
    async def echo(self, ctx, *args):
        channel = ctx.message.channel
        author = ctx.message.author
        print('Echo command used by: ' + str(ctx.message.author))
        # 486395977373319168
        if discord.utils.get(author.roles, name="Staff"):
            output = ''
            for word in args:
                output += word
                output += ' '
            embed = discord.Embed(
                title='Announcement',
                description=output,
                colour=discord.Colour.blue()
            )
            embed.set_footer(text="Bot created by harryjoseph#3275")
            embed.set_thumbnail(url='https://i.imgur.com/LX8d1xH.jpg')
            embed.set_author(name='SADPS Bot',
                             icon_url='https://i.imgur.com/LX8d1xH.jpg')
            await channel.send(embed=embed)
        else:
            await channel.send('You do not have permission to use this command.')

    @commands.command(pass_context=True)
    @commands.guild_only()
    async def kick(self, ctx, user: discord.Member, *, reason):
        channel = ctx.message.channel
        author = ctx.message.author
        guild = ctx.message.guild
        print('{0} has been kicked by {1}'.format(user, author))
        if discord.utils.get(author.roles, name="Staff"):
            if guild.id == 473977440603996164:
                if user == author:
                    await channel.send("You cannot kick yourself, that's daft.")
                else:
                    await user.send("You have been kicked because of: {0}".format(reason))
                    await author.send('You have kicked {0}'.format(user))
                    await guild.kick(user, reason=reason)
                    await channel.send("User has been kicked")
                    print('{0} has been kicked by {1}'.format(user, author))
            else:
                await channel.send("This command cannot be used within this server.")
        else:
            await channel.send("You do not have permission to use this command.")

    async def reportdb(self):
        async with aiosqlite.connect('utils/bot.db') as db:
            await db.execute('''CREATE TABLE reports
                (id int, user int, date date, body text)''')
            await db.commit()

    async def reportinsert(self, user, reason):
        async with aiosqlite.connect('utils/bot.db') as db:
            d = datetime.now().strftime("%Y-%m-%d %H:%M")
            await db.execute('INSERT INTO reports (user, date, body) VALUES ("{0}", "{1}", "{2}")'.format(user, d, reason))
            await db.commit()

    async def reportquery(self, id):
        async with aiosqlite.connect('utils/bot.db') as db:
            db.row_factory = aiosqlite.Row
            sql = 'SELECT * FROM reports WHERE id = ?'
            cursor = await db.execute(sql, (id,))

            row = await cursor.fetchone()
            rows = await cursor.fetchall()
            await cursor.close()
            if id == 0:
                sql = 'SELECT * FROM reports'
                cursor = await db.execute(sql)

                rows = await cursor.fetchall()
                return rows
            else:
                sql = 'SELECT * FROM reports WHERE id = ?'
                cursor = await db.execute(sql, (id,))

                row = await cursor.fetchone()
                return row

    async def reportRowDelete(self, id):
        async with aiosqlite.connect('utils/bot.db') as db:
            sql = 'DELETE FROM reports WHERE id = ?'
            cursor = await db.execute(sql, (id,))
            await db.commit()

            await cursor.close()

    @commands.command(aliases=['record', 'reports'])
    @commands.guild_only()
    async def records(self, ctx, id=0):
        embed = discord.Embed(
            title='Reports',
            colour=discord.Colour.red()
        )
        embed.set_footer(text="Bot created by harryjoseph#3275")
        embed.set_thumbnail(url='https://i.imgur.com/LX8d1xH.jpg')
        embed.set_author(name='SADPS Bot',
                         icon_url='https://i.imgur.com/LX8d1xH.jpg')
        if discord.utils.get(ctx.author.roles, name="Staff"):
            if id == 0:
                rows = await self.reportquery(id)
                for row in rows:
                    embed.add_field(
                        name=f"ID: {row['id']}", value=f"from: {self.bot.get_user(row['user'])}")
                await ctx.send(embed=embed)
            else:
                row = await self.reportquery(id)
                username = self.bot.get_user(row['user'])
                report = row['body']
                date = row['date']
                embed.add_field(
                    name="User:", value=f"{username}", inline=False)
                embed.add_field(
                    name="Report:", value=f"{report}", inline=False)
                embed.add_field(name="Date:", value=f"{date}", inline=False)
                await ctx.send(embed=embed)
        else:
            await ctx.send("You must be staff to use this command.")

    @commands.command()
    async def report(self, ctx, *, reason):
        user = ctx.author.id
        reportChat = ctx.guild.get_channel(526810175655510016)

        embed = discord.Embed(
            title='Reports',
            colour=discord.Colour.red()
        )
        embed.set_footer(text="Bot created by harryjoseph#3275")
        embed.set_thumbnail(url='https://i.imgur.com/LX8d1xH.jpg')
        embed.set_author(name='SADPS Bot',
                         icon_url='https://i.imgur.com/LX8d1xH.jpg')
        embed.add_field(
            name=f"Report from: {ctx.author.nick}", value=f"{reason}", inline=False)

        await self.reportinsert(user, reason)
        await ctx.message.delete()
        await ctx.send(":white_check_mark: Your report has been sent, it will be reviewed soon.")
        await reportChat.send(embed=embed)

    @commands.command(aliases=['report-delete', 'report-remove', 'del-report'])
    async def reportdelete(self, ctx, id):
        if discord.utils.get(ctx.author.roles, name="Staff"):
            await self.reportRowDelete(id)
            await ctx.send(f"Report ID: {id} has been removed.")
        else:
            await ctx.send("You must be staff to use this command.")

    @commands.command()
    @commands.guild_only()
    async def strike(self, ctx, user: discord.Member, *, reason):
        strikeOne = discord.utils.get(ctx.guild.roles, name="X")
        strikeTwo = discord.utils.get(ctx.guild.roles, name="XX")
        strikeThree = discord.utils.get(ctx.guild.roles, name="XXX")
        if discord.utils.get(ctx.author.roles, name="Staff"):
            if discord.utils.get(ctx.guild.roles, name="X"):
                if discord.utils.get(user.roles, name="X"):
                    await ctx.send("The strike has been assigned!")
                    await user.add_roles(strikeTwo, reason=reason, atomic=True)
                    await user.send(f"You have been given your second strike because: {reason}. If you would wish to know why speak to a Junior Staff Member.")
                elif discord.utils.get(user.roles, name="XX"):
                    await ctx.send("The strike has been assigned!")
                    await user.add_roles(strikeThree, reason=reason, atomic=True)
                    await user.send(f"You have been given your third strike because: {reason}. If you would wish to know why speak to a Junior Staff Member. However, this is your FINAL warning.")
                elif discord.utils.get(user.roles, name="XXX"):
                    await ctx.send("This user has already recieved 3 strikes, consult with the staff team for the next stage.")
                else:
                    await ctx.send("The strike has been assigned!")
                    await user.add_roles(strikeOne, reason=reason, atomic=True)
                    await user.send(f"You have been given your first strike because: {reason}. If you would wish to know why speak to a Junior Staff Member.")
            else:
                await ctx.send("This server does not have the 'X' role.")
        else:
            await ctx.send("You're not a staff :o !")


def setup(bot):
    bot.add_cog(Moderate(bot))
