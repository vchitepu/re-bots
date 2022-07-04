import os
import discord
import modules.cryptoapi as crypto

client = discord.Client()

@client.event
async def on_ready():
	print("We have logged in as {0.user}".format(client))

async def on_message():

	if message.channel.id == 993665883102777444:

		if message.content.startswith('$price'):
			await message.channel.send(message.content)
		

client.run(os.getenv('CYPTO_BOT_SECRET'))