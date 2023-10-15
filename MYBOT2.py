intents=discord.Intents.default()
intents.message_content=True
bot=commands.Bot(command_prefix="$",intents=intents)
@bot.event
async def on_message(message):
    if message.author==bot.user:
        return
    if message.content.startswith("$selam"):
        await message.channel.send("naber")
    elif message.content.startswith("$kimseniyaptı"):
        await message.channel.send("Tuna adlı bir arkadaş yaptı")
    elif message.content.startswith("$dolarkaçtl"):
        await message.channel.send("tyyp olduğu sürece fazla")
    elif message.content.startswith("$neleryaparsın"):
        await message.channel.send("Tuna bana ne yazdıysa")
    elif message.content.startswith("code#9888open"):
        await message.channel.send("mybot.py/#scmrfwct")
    else:
        await message.channel.send("O kadar kelime bilmiyom")
bot.run("MTE1ODgxODYxMjU4OTYzMzU2Ng.G4IzRy.pYkGdyqhk8ZAEuovm8ScDRLRKp-4Lzm1Opaa8o")
