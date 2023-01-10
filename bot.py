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

userCoins = {}

with open('bagridbucks.json','r') as j:
    userCoins = json.load(j)


def giveCoins(id):
    randAdd = random.randint(5,10)
    if id in userCoins.keys():
        userCoins[id] = userCoins[id] + randAdd
    else:
        userCoins[id] = randAdd

    jsonObj = json.dumps(userCoins, indent=4)
    with open('bagridbucks.json','w') as outfile:
        outfile.write(jsonObj)

    return randAdd


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    authorId = str(message.author.id)

    if message.content.lower().startswith('bucks'):
        coinies = 0
        if authorId in userCoins.keys():
            coinies = userCoins[str(authorId)]
        await message.channel.send('You have '+str(coinies)+' BagridBucks!')
        return

    bagriddy = False

    for word in message.content.split(' '):
        word = re.sub(r'[^a-zA-Z]', '', word)
        if word.lower() == 'bagrid':
            bagriddy = True
    
    if bagriddy:
        await message.channel.send(random.choice(responses))
        if random.randint(1,10) == 1:
            coinsAdded = giveCoins(authorId)
            await message.channel.send('You earned '+str(coinsAdded)+' BagridBucks!')

client.run(TOKEN)
