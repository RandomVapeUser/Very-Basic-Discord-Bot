from datetime import timedelta, datetime
from discord.ext import commands
import discord
import config


Entries = 0
Entries_list = []

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=f"{config.data['Prefix']}", intents=discord.Intents.all())
bot.remove_command("help")
bot.remove_command("reload")

channelid = config.data['ChannelID']

#Welcomer
async def sender(ctx, member: discord.Member):
    avatar = member.avatar.url
    description = "ConfigHub is a place where you can talk about cheats and discuss about configs!"
    embed = discord.Embed()
    embed.set_author(name=f"{member.name}", icon_url=f"{avatar}")
    embed.set_thumbnail(url=avatar)
    embed.add_field(name="Welcome to ConfigHub!", value=f"{description}", inline=False)
    channel = bot.get_channel(channelid)
    await channel.send(member.mention,embed=embed)
        
#Permissions Check
async def perms(ctx):
    perm = ctx.author.guild_permissions.kick_members
    if perm == False:
        await ctx.send("You do not have the neccessary permissions (fuck off)")
        return True
    else:
        return False
        
#----------------------------------------------------------------------------------------------------------
    
@bot.event
async def on_member_join(member: discord.Member):
    member2 = member
    await sender(member2,member2)

@bot.command()
async def reload(ctx):
    await bot.unload_extension("cmds.gay")
    await bot.load_extension("cmds.gay")
    await bot.unload_extension("cmds.addalt")
    await bot.load_extension("cmds.addalt")
    await bot.unload_extension("cmds.kick")
    await bot.load_extension("cmds.kick")
    await bot.unload_extension("cmds.ban")
    await bot.load_extension("cmds.ban")
    await bot.unload_extension("cmds.unban")
    await bot.load_extension("cmds.unban")
    await bot.unload_extension("cmds.mute")
    await bot.load_extension("cmds.mute")
    await bot.unload_extension("cmds.unmute")
    await bot.load_extension("cmds.unmute")
    await bot.unload_extension("cmds.pfp")
    await bot.load_extension("cmds.pfp")
    await bot.unload_extension("cmds.serverinfo")
    await bot.load_extension("cmds.serverinfo")
    await bot.unload_extension("cmds.admin")
    await bot.load_extension("cmds.admin")
    await bot.unload_extension("cmds.help")
    await bot.load_extension("cmds.help")
    await bot.unload_extension("cmds.video")
    await bot.load_extension("cmds.video")
    await bot.unload_extension("cmds.purge")
    await bot.load_extension("cmds.purge")
    await bot.unload_extension("cmds.giveaway")
    await bot.load_extension("cmds.giveaway")
    await bot.unload_extension("cmds.say")
    await bot.load_extension("cmds.say")
    await bot.get_channel(channelid).send(f"Extensions Reloaded")

@bot.event
async def on_ready():
    await bot.load_extension("cmds.gay")
    await bot.load_extension("cmds.addalt")
    await bot.load_extension("cmds.kick")
    await bot.load_extension("cmds.ban")
    await bot.load_extension("cmds.unban")
    await bot.load_extension("cmds.mute")
    await bot.load_extension("cmds.unmute")
    await bot.load_extension("cmds.pfp")
    await bot.load_extension("cmds.serverinfo")
    await bot.load_extension("cmds.admin")
    await bot.load_extension("cmds.help")
    await bot.load_extension("cmds.video")
    await bot.load_extension("cmds.purge")
    await bot.load_extension("cmds.giveaway")
    await bot.load_extension("cmds.say")
    channel = bot.get_channel(channelid)
    await channel.send("Extensions Loaded")

config.data["Online"] = True
bot.run(config.data["Token"])



