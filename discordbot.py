# This example requires the 'message_content' intent.

import keys
import discord
from main import request

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$tweet"):
        await message.channel.send(request())


client.run(keys.TOKEN)
