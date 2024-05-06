from discord.ext import commands
import asyncio
import discord

@commands.hybrid_command(aliases=["clear","Purge"])
async def purge(ctx, number = None):
    nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)
    if ctx.author.guild_permissions.kick_members == True:
        embed = discord.Embed(title="Purge Command",description="")
        embed.add_field(name="", value="`>> ?purge all`",inline=True)
        embed.add_field(name="", value="`>> ?Purge [amount]`",inline=False)
        if number == None:
            await ctx.reply(embed=embed)
        elif number == "all" or number == "All":
            new_channel = await nuke_channel.clone(reason="Has been Nuked!")
            await nuke_channel.delete()
            await ctx.send(f"purged by `{ctx.author}`")
        elif number != None:
            await ctx.send(f"`Purging {number} messages.`")
            await asyncio.sleep(1)
            await ctx.channel.purge(limit=int(number) + 2)

async def setup(bot):
    bot.add_command(purge)