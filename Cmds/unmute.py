from discord.ext import commands
from datetime import timedelta, datetime
import time
import discord

async def perms(ctx):
    perm = ctx.author.guild_permissions.kick_members
    if perm == False:
        await ctx.send("You do not have the neccessary permissions (fuck off)")
        return True
    else:
        return False

@commands.hybrid_command()
async def unmute(ctx, user:discord.Member):
    if await perms(ctx) == True:
        return
    try:
        await user.edit(timed_out_until=None)
        await ctx.send(f"Removed timeout from {user}")
    except Exception as i:
        await ctx.send(i)

async def setup(bot):
    bot.add_command(unmute)