import os
from discord.ext import commands

async def perms(ctx):
    perm = ctx.author.guild_permissions.kick_members
    if perm == False:
        await ctx.send("You do not have the neccessary permissions (fuck off)")
        return True
    else:
        return False

@commands.hybrid_command()
async def addalt(ctx, name = None):
    if await perms(ctx) == True:
        return
    if name == None:
        await ctx.send("Provide alt name.")
        return
    path = './alts.txt'
    check_file = os.path.isfile(path)
    try:
        if check_file == True:
            with open("alts.txt", "w") as file:
                file.write(f"{name}\n")
                file.close()
                await ctx.send(f"Alt {name} saved to files!")
        else:
            with open("alts.txt", "a") as file:
                file.write(f"{name}\n")
                file.close()
                await ctx.send(f"Alt {name} saved to files!")
    except Exception as i:
        await ctx.send(i)

async def setup(bot):
    bot.add_command(addalt)