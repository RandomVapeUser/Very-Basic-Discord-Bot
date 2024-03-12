import discord
import random
from discord.ext import commands

async def perms(ctx):
    perm = ctx.author.guild_permissions.kick_members
    if perm == False:
        await ctx.send("You do not have the neccessary permissions (fuck off)")
        return True
    else:
        return False

@commands.hybrid_command()
async def unban(ctx, id: int = None):
    if await perms(ctx) == True:
        return
    if user == None:
        await ctx.send("User is required")
    try:
        user = await bot.fetch_user(id)
        await ctx.guild.unban(user)
        embed = discord.Embed()
        embed.add_field(name="", value = f"Unbanned {user}", inline = False)
        await ctx.send(embed=embed)
    except Exception as i:
        await ctx.send(i)

async def setup(bot):
    bot.add_command(unban)