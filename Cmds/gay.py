import discord
import random
from discord.ext import commands

@commands.hybrid_command()
async def gay(ctx, user:discord.Member = None):
    user == user
    if user == "sentre_not_termed":
        embed.add_field(name=f"{ctx.author} is:", value=f"**99% gay**", inline=False)
        await ctx.send(embed=embed)
        return
    if user != None:
        try:
            while True:
                value = random.randint(0, 100)
                embed = discord.Embed()
                embed.add_field(name=f"{ctx.author} is:", value=f"**{value}% gay**", inline=False)
                await ctx.send(embed=embed)
                return
        except Exception as i:
            await ctx.send(i)
    elif user == None:
        value = random.randint(0,100)
        embed = discord.Embed()
        embed.add_field(name=f"{ctx.author} is:", value=f"**{value}% gay**", inline=False)
        await ctx.send(embed=embed)
        return

async def setup(bot):
    bot.add_command(gay)
