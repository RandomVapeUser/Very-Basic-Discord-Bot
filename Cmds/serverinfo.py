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
async def serverinfo(ctx):
    datetime = datetime.now
    embed = discord.Embed(title="Information about ConfigHUB")
    embed.add_field(name="**Name:**", value="ConfigHub (not real)", inline=False)
    embed.add_field(name="**Owner**", value=f"@{ctx.guild.owner_id}", inline=False)
    embed.add_field(name="**ID:**", value="1194623585977909398", inline=False)
    embed.add_field(name="**Membercount:**", value=f"{discord.member_count}", inline=False)
    embed.add_field(name="**TextChannelcount:**", value=f"{ctx.guild.textchannel_count}", inline=False)
    embed.add_field(name="**VoiceChannelcount:**", value=f"{discord.VoiceChannel}", inline=False)
    embed.add_field(name="**Boostercount:**", value=f"{ctx.guild.premium_subscription_count}", inline=False)
    embed.add_field(name="**Booster tier**", value=f"{ctx.guild.premium_subscription_tier}", inline=False)
    embed.add_field(name="**Created at**", value=f"{datetime}", inline=False)
    try:
        await ctx.send(embed=embed)
    except Exception as i:
        await ctx.send(i)

async def setup(bot):
    bot.add_command(serverinfo)

