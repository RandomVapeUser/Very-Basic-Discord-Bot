from discord.ext import commands
import discord

async def perms(ctx):
    perm = ctx.author.guild_permissions.kick_members
    if perm == False:
        await ctx.send("You do not have the neccessary permissions (fuck off)")
        return True
    else:
        return False

@commands.hybrid_command()
async def video(ctx, link):
    if await perms(ctx) == True:
        return
    answer = f"everyone, Sal has released a new video! {link}"
    await ctx.channel.purge(limit=1)
    await ctx.send(answer)

async def setup(bot):
    bot.add_command(video)