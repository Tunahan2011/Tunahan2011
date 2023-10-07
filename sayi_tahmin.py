import discord
import random
import asyncio


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Geldik bea {self.user} (ID al: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('$tahminet'):
            await message.channel.send("1'den 10'a kadar bi sayı tutayum sen bileysun 10 saniye uçunde")

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 10)

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=10.0)
            except asyncio.TimeoutError:
                return await message.channel.send(f'Buyuk dedun doğrusu {answer}.')

            if int(guess.content) == answer:
                await message.channel.send('Doğru deysun.')
            else:
                await message.channel.send(f'Kuçuk bildun doğrusu {answer}.')


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTE1ODgxODYxMjU4OTYzMzU2Ng.GGWEdf.W-XIAPFjHFlhELQYWugRF1GOsb_KKWOk6f4qm8')
