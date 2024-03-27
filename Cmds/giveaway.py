from discord import Button, ButtonStyle
from datetime import datetime
from discord.ext import commands
import discord
import asyncio
import emoji
import random

@commands.hybrid_command()


async def gw(ctx, time = None, description = None, prize = None):

    Entries = 0
    Entries_list = []
    reaction = "🎉"

    original_time = time
    separated_list = list(time)
    int_time = int(separated_list[0])
    total = {"s": 1, "m": 60, "h": 3600, "d": 86400}
    total_time = int_time * total[separated_list[1]]
    time = total_time

    datetime_now = datetime.now()

    embed = discord.Embed()
    embed.add_field(name=f"{prize}", value=f"{description}", inline=False)
    embed.add_field(name="Ends in: ", value=f"{time}", inline=True)
    embed.add_field(name="Hosted by: ", value=f"{ctx.author.mention}", inline=True)
    embed.add_field(name="Entries: ", value=f"{Entries}", inline=True)
    embed.add_field(name="Created in: ", value=f"{datetime}", inline=True)
    send_embed = await ctx.send(embed=embed)
    while time > 0:
        embed2 = discord.Embed()
        embed2.add_field(name=f"{prize}", value=f"{description}", inline=False)
        embed2.add_field(name="Ends in: ", value=f"{original_time}({time})", inline=True)
        embed2.add_field(name="Hosted by: ", value=f"{ctx.author.mention}", inline=True)
        embed2.add_field(name="Entries: ", value=f"{Entries}", inline=True)
        embed2.add_field(name="Created in: ", value=f"{datetime_now}", inline=True)
        final_embed = await send_embed.edit(embed=embed2)
        await final_embed.add_reaction(reaction)
        await asyncio.sleep(1)
        time -= 1
    else:
        users = await embed2.reactions[0].users().flatten()
        choice =  random.choice(users)
        print(choice)



async def setup(bot):
    bot.add_command(gw)

