from discord.ext import commands
import discord
import os

async def perms(ctx):
    perm = ctx.author.guild_permissions.kick_members
    if perm == False:
        await ctx.send("You do not have the neccessary permissions (fuck off)")
        return True
    else:
        return False

@commands.hybrid_command()
async def alts(ctx):
    if await perms(ctx) == True:
        await ctx.send("No alts for you!")
        return
    path = './alts.txt'
    if os.path.isfile(path) == False:
        await ctx.send("Please create an altx.txt file")
        return
    else:
        with open(path, 'r') as file:
            alts_list = file.readlines()
        embed = discord.Embed(title="Hypixel Alts Banned/Unbanned", description="")
        for index, alt in enumerate(alts_list, start=1):
            embed.add_field(name=f"Alt {index}", value=alt.strip(), inline=False)
        await ctx.send(embed=embed)

async def setup(bot):
    bot.add_command(alts)