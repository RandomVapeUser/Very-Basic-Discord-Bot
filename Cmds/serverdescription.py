from discord.ext import commands

@commands.hybrid_command()
async def serverdescription(ctx,description):
    server_name = ctx.guild.name
    with open(f"{server_name}.txt", "w") as file:
        file.write(description)
        await ctx.send("Updated Welcomer Description!")

async def setup(bot):
    bot.add_command(serverdescription)

