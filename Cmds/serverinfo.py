from discord.ext import commands
from datetime import datetime
import discord


async def perms(ctx):
    perm = ctx.author.guild_permissions.kick_members
    if perm == False:
        await ctx.send("You do not have the neccessary permissions (fuck off)")
        return True
    else:
        return False

@commands.hybrid_command()
async def serverinfo(ctx):
    dateTime = ctx.guild.created_at.strftime("%Y-%m-%d %H:%M:%S")
    embed = discord.Embed(title="Server Info")
    embed.add_field(name="Name:", value="`ConfigHub (not real)`", inline=True)
    embed.add_field(name="Owner:", value=f"`{ctx.guild.owner_id}`", inline=True)
    embed.add_field(name="Server ID:", value=f"`{ctx.guild.id}`", inline=True)
    embed.add_field(name="Member count:", value=f"`{ctx.guild.member_count}`", inline=True)
    embed.add_field(name="Text Channels:", value=f"`{len(ctx.guild.text_channels)}`", inline=True)
    embed.add_field(name="Voice Channels:", value=f"`{len(ctx.guild.voice_channels)}`", inline=True)
    embed.add_field(name="Created at:", value=dateTime, inline=True)
    await ctx.send(embed=embed)

async def setup(bot):
    bot.add_command(serverinfo)

