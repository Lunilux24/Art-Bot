# This example requires the 'message_content' intent.

import keys
import discord
from main import get_tweet_id

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
        await message.channel.send(f"https://twitter.com/user/status/{get_tweet_id()}")


client.run(keys.token)
