import discord
import json
import random

data = {}
intents = discord.Intents.default()
intents.message_content = True

responses = [
    "*curls up in a ball on the tower doorstep*",
    "Are you *sure* these are berries?",
    'Hit the bagriddy',
    'Can you tell me about your establishment for my friends over there? *gestures vaguely behind him*',
    "I'm not your dad!",
    "Can we make this quick? I have to wrestle a shark at 5.",
    "*simps for lodona*",
    "I'm having trouble confronting my true feelings for Gunky Rick.",
    "You wouldn't know the first thing about rizz. Watch and learn.",
    "You unlocked the secret Bagrid response! You win an iPad. Please send your mother's maiden name and credit card info to bigbundabagrid@gmail.com",
    "Have I ever shown you my water cube?",
    "Ok so I have this really cool thing I can do where basically I can control water and- wait where are you going?"
]

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
    
    if bagriddy:
        await message.channel.send(random.choice(responses))

client.run(TOKEN)
