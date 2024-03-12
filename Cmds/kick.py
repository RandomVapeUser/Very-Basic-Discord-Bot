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
async def kick(ctx, user:discord.Member, reason = "No Reason"):
    if await perms(ctx) == True:
        return
    if user == None:
        await ctx.send("User is required")
    try:
        await user.kick()
        embed= discord.Embed()
        embed.add_field(name=f"Kicked {user}", value=f"Reason : {reason}", inline=False)
        await ctx.send(embed=embed)
    except Exception as i:
        await ctx.send(i)

async def setup(bot):
    bot.add_command(kick)