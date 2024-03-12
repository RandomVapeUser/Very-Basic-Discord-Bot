from discord.ext import commands
import discord

async def say(ctx, content = None):
    if content == None:
        embed = discord.Embed()
        embed.add_field(name="?say command", value= "Usage: ?say [content]", inline=False)
    else:
        await ctx.channel.purge(limit=1)
        await ctx.channel.send(content)

async def setup(bot):
    bot.add_command(say)