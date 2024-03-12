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
async def mute(ctx, member: discord.Member, time):
    if await perms(ctx) == True:
        return
    try:
        separated_list = list(time)
        int_time = int(separated_list[0])
        total = {"s": 1, "m": 60, "h": 3600, "d": 86400}
        total_time = int_time * total[separated_list[1]]
        
        if member is None:
            await ctx.send("The correct usage for this command is:\n**||?mute [USER] [TIME]||**")
            return

        seconds = 0
        minutes = 0
        hours = 0
        days = 0

        if separated_list[1] in total:
            total_seconds = int_time * total[separated_list[1]]
            duration = timedelta(seconds=total_seconds)
            await member.timeout(duration)
            await ctx.send(f"Muted {member} for {duration}")
        else:
            await ctx.send("You can only use s,m,h and d are you dumb?")
    except Exception as i:
        await ctx.send(f"{i}")

async def setup(bot):
    bot.add_command(mute)