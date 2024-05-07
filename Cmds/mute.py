from discord.ext import commands
from datetime import datetime
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
    if member is None:
            embed = discord.Embed()
            embed.add_field(name="Mute command",value="`?mute {member} {duration}`")
            return
    
    try:
        time_str = time.lower()
        if time_str[-1] not in ('s', 'm', 'h', 'd'):
            await ctx.send("Time not found use s,m,h and d.")
            return
        
        duration_unit = time_str[-1]
        duration_value = int(time_str[:-1])

        total_seconds = {
            's': duration_value,
            'm': duration_value * 60,
            'h': duration_value * 3600,
            'd': duration_value * 86400
        }.get(duration_unit)
        with open("time.txt","w+") as f:
            f.write(f"{total_seconds}")
            f.close()
        seconds = 0
        minutes = 0
        hours = 0
        days = 0
        
        with open("time.txt","r") as f:
            for i in f:
                await member.timeout(i)
                await ctx.send("Timeouted!")
        await ctx.send(f"Muted {member} for {total_seconds}")
    except Exception as i:
        await ctx.send(f"{i}")

async def setup(bot):
    bot.add_command(mute)