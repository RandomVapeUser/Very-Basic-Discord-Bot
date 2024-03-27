from discord.ext import commands
import discord

@commands.hybrid_command()
async def say(ctx, content = None):
    Z = 1
    total = []
    if content == None:
        embed = discord.Embed()
        embed.add_field(name="?say command", value= "Usage:")
        embed.add_field(name="",value=">> ?say [Message]")
    else:
        await ctx.channel.purge(limit=1)
        final_content = content.split()
        await ctx.send(final_content)
        for i in final_content:
            total.append(final_content[Z])
        await ctx.send(total)

async def setup(bot):
    bot.add_command(say)