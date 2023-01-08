import discord
import json

data = {}
intents = discord.Intents.default()
intents.message_content = True

with open('config.json', 'r') as f:
  data = json.load(f)


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
        if word.lower() == 'bagrid':
            bagriddy = True

client.run(TOKEN)