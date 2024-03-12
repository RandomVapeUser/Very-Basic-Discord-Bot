from discord.ext import commands
import discord

@commands.hybrid_command()
async def pfp(ctx, user : discord.Member = None):
    if user == None:
        await ctx.send("No user provided")
        return
    else:
        pfp = user.avatar.url
        embed = discord.Embed()
        embed.set_image(url=pfp)
        await ctx.send(embed=embed)

async def setup(bot):
    bot.add_command(pfp)