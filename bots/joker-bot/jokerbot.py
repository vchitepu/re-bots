import os
import discord
import modules.jokesapi as joke

client=discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):

    if message.channel.id == 988194405062180924:

        if message.author == client.user:
            return

        if message.content.startswith('tell me a joke'):
            await message.channel.send(joke.get_random_joke())


client.run(os.getenv('JOKER_BOT_SECRET'))
