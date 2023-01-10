import discord
import json
import random
import re

data = {}
intents = discord.Intents.default()
intents.message_content = True

with open('config.json', 'r') as f:
  data = json.load(f)

with open('responses.txt', 'r') as k:
    responses = k.readlines()
    
TOKEN = data['token']

print(data)
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    bagriddy = False
    for word in message.content.split(' '):
        word = re.sub(r'[^a-zA-Z]', '', word)
        if word.lower() == 'bagrid':
            bagriddy = True
    
    if bagriddy:
        await message.channel.send(random.choice(responses))

client.run(TOKEN)
