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
async def admin(ctx):
    if await perms(ctx) == True:
        return
    embed = discord.Embed(title="**Permissions Dashboard**", description=None)
    embed.add_field(name="Rank: ", value=f"**||{ctx.author.top_role}||**", inline=False)
    embed.add_field(name=">> Ban Members: ", value=f"{ctx.author.guild_permissions.ban_members}", inline=False)
    embed.add_field(name=">> Kick Members: ", value=f"{ctx.author.guild_permissions.kick_members}", inline=False)
    await ctx.send(embed=embed)
    
async def setup(bot):
    bot.add_command(admin)