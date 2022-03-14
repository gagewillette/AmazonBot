from discord.ext import commands
from fetchlink import main

bot = commands.Bot(command_prefix="!")

@bot.command()
async def link(ctx):
    str = await main()

    await ctx.send(str)

bot.run("NTA4Njk2MDk1OTQxOTg0MjY1.W98uKA.zSp3wa2keOY9m5o0MdKura8SBvQ")