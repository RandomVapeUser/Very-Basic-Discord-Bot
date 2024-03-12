from discord.ext import commands
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
async def purge(ctx, number = None):
    if await perms(ctx) == True:
        return
    if number == None:
        embed = discord.Embed()
        embed.add_field(name="Purge Command:", value="Usage: ?Purge [Number] or ?Purge all.")
        await ctx.send(embed=embed)
    if number != "all":
        try:
            Z = int(number)
            await ctx.send(f"Purging {Z} messages....")
            time.sleep(2)
            await ctx.channel.purge(limit=Z+2)
        except Exception as i:
            await ctx.send("r u dumb? u cant purge words")
            time.sleep(2)
    else:
        await ctx.channel.purge()
        await ctx.send(f"Channel Purged by @{ctx.author}")

async def setup(bot):
    bot.add_command(purge)