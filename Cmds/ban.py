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
async def ban(ctx, user:discord.Member = None, reason = "No Reason"):
    if await perms(ctx) == True:
        return
    if user == None:
        embed = discord.Embed()
        embed.add_field(name="Ban Command", value="Usage: ?Ban [User].")
        await ctx.send(embed=embed)
    try:
        await user.ban()
        embed = discord.Embed()
        embed.add_field(name=f"Banned {user}", value = f"Reason: {reason}", inline = False)
        await ctx.send(embed=embed)
    except Exception as i:
        await ctx.send(i)

async def setup(bot):
    bot.add_command(ban)