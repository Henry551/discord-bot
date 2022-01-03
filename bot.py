import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="[")


@bot.event
async def on_ready():
    print(">>bot is online<<")


bot.run("OTI3NDgyNDU4MTA1MDYxNDA3.YdK3WQ.gSurzzo55facb-kxoasSQxMDoQo")
