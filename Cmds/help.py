from discord.ext import commands
import discord

@commands.hybrid_command()
async def help(ctx):
    description = "Available comands for CheatBot"
    embed = discord.Embed(title="Bot Comands",description=f"{description}", colour=0x00C5FF)
    embed.add_field(name="**?Mute [@Member] [Reason]**", value="|| || Admin || Banned member with reason or no.", inline=False)
    embed.add_field(name="", value="-------------------------------------------------------------", inline=False)
    embed.add_field(name="**?Video [Video Link]**", value="|| || Admin || Pings everyone to announce a video.", inline=False)
    embed.add_field(name="", value="-------------------------------------------------------------", inline=False)
    embed.add_field(name="**?pfp [@Member]**", value="Shows an user pfp you dont need to ping them you can use their username", inline=False)
    embed.add_field(name="", value="-------------------------------------------------------------", inline=False)
    embed.add_field(name="**?Purge [Amount of messages]**", value="|| || Admin || Deletes an amount of messages or all.", inline=False)
    embed.add_field(name="", value="-------------------------------------------------------------", inline=False)
    embed.add_field(name="**?Unmute [@Member]**", value="|| || Admin || Unmutes a member.",inline=False)
    embed.add_field(name="", value="-------------------------------------------------------------", inline=False)
    embed.add_field(name="**?gw [Item] [Time] [Description]**", value="Giveaway comand, temporarily unavailable, requires all parameters", inline=False)
    embed.add_field(name="", value="-------------------------------------------------------------", inline=False)
    embed.add_field(name="**?addalt [ALT NAME]**", value="Add an alt to the alts file.", inline=False)
    embed.add_field(name="", value="-------------------------------------------------------------", inline=False)
    embed.add_field(name="**?alts**", value="Shows alts.", inline=False)
    await ctx.send(embed=embed)

async def setup(bot):
    bot.add_command(help)
