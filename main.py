from datetime import timedelta, datetime
from discord.ext import commands
from discord.utils import get
import random
import discord
import config
import asyncio
import os


Entries = 0
Entries_list = []

intents = discord.Intents.default()
intents.message_content = True
intents.all()

bot = commands.Bot(command_prefix=f"{config.data['Prefix']}", intents=discord.Intents.all())
bot.remove_command("help")
bot.remove_command("reload")


    
#Dependant Function for other commands-----------------------------------------------------------------
channelid = 1215782656923402280
#Welcomer
async def sender(ctx, member: discord.Member):
    server_name = member.guild.name
    avatar = member.avatar.url
    while True:
        try:
            with open(f"{server_name}.txt", "r+") as file:
                description = file.read().rstrip()
                if description == "":
                    description = "Server Description is empty. Please set one with ?ServerDes [Description]"

                embed = discord.Embed(description=server_name, color=0xFF5733)
                embed.set_author(name=f"Welcome to ConfigHub, {member.name}!", icon_url=avatar)
                embed.add_field(name="", value=f"{description}", inline=False)
                embed.set_thumbnail(url=avatar)
                
                cheathub_channel_id = 1215766481183178964 
                cheat_hub_serverid = 1194623585977909398
                fanex_channel_id = 1224809925792764046
                fanex_server_id = 1211779040684412969
                checkid = member.guild.id
                if checkid == cheat_hub_serverid:
                    channel_id = cheathub_channel_id
                if checkid == fanex_server_id:
                    channel_id = fanex_channel_id
                channel2 = ctx.guild.get_channel(channel_id)
                if channel2:
                    await channel2.send(embed=embed)
                else:
                    print(f"Channel with ID {channel_id} not found.")
                break
        except FileNotFoundError:
            with open(f"{server_name}.txt", "w") as file:
                file.write("")
            continue

        
#Permissions Check
async def perms(ctx):
    perm = ctx.author.guild_permissions.kick_members
    if perm == False:
        await ctx.reply("Missing Permissions", mention_author = False)
        return True
    else:
        return False
        
#----------------------------------------------------------------------------------------------------------
    
@bot.event
async def on_member_join(member: discord.Member):
    await sender(member,member)

@bot.command()
async def reload(ctx):
    await bot.unload_extension("cmds.role")
    await bot.load_extension("cmds.role")
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
    try:
        datetime_final = datetime.now()
        await bot.load_extension("cmds.role")
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
        await channel.send(f"Bot Started | {datetime_final}")
    except Exception as i:
        await bot.get_channel(channelid).send("The Bot has crashed, check latest log.")
        with open("latest.txt", "a+") as log:
            log.write(f"{datetime_final} | {i}\n")
            log.close()
    
config.data["Online"] = True
bot.run(config.data["Token"])



