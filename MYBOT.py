import discord
from discord.ext import commands
import random as r
import os
intents=discord.Intents.default()
intents.message_content=True
bot=commands.Bot(command_prefix="#",intents=intents)
n=0
@bot.event
async def on_ready():
    print(f"Geldik {bot.user}")
@bot.command()
async def hayvanlar(ctx):
    
    gorsel1=r.choice(os.listdir("animals"))
    with open(f"animals/{gorsel1}","rb") as f:
        resim1=discord.File(f)
    await ctx.send(file=resim1)

@bot.command()
async def bitkiler(ctx):
    gorsel2=r.choice(os.listdir("plants"))
    with open(f"plants/{gorsel2}","rb") as e:
        resim2=discord.File(e)
    await ctx.send(file=resim2)

@bot.command()
async def robotlar(ctx):
   
    gorsel3=r.choice(os.listdir("robots"))
    with open(f"robots/{gorsel3}","rb") as g:
        resim3=discord.File(g)
    await ctx.send(file=resim3)
@bot.command()
async def scmrfwct(ctx):
    with open(("smurfkedi.jpeg"),"rb") as d:
        resim4=discord.File(d)
    await ctx.send(file=resim4)

    
bot.run("MTE1ODgxODYxMjU4OTYzMzU2Ng.G4IzRy.pYkGdyqhk8ZAEuovm8ScDRLRKp-4Lzm1Opaa8o")
