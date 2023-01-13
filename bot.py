import discord
import json
import random
import re

data = {}
intents = discord.Intents.default()
intents.message_content = True

purchases = {
    'Bagrid Premium':[50,'For when you need that extra bagriddy goodness in your life.','P'],
    'Bagrid Doubler':[250,'Oh god, now there are two of them!','D'],
    'Bagrid Confidence Booster':[500,"Bagrid has found confidence in himself at last!",'C']
}

with open('config.json', 'r') as f:
    data = json.load(f)

with open('responses.txt', 'r') as k:
    responses = k.readlines()
    
TOKEN = data['token']

print(data)
client = discord.Client(intents=intents)

userCoins = {}
userItems = {}

with open('bagridbucks.json','r') as j:
    userCoins = json.load(j)

with open('items.json','r') as file:
    userItems = json.load(file)


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

async def showShop(id,message):
    out = 'Here are the items available for purchase:'
    if id in userItems.keys():
        userHas = userItems[id]
    else:
        userItems[id] = []
        userHas = []
    counter = 0
    for item in purchases.keys():
        if item not in userHas:
            out += '\n'
            out += f'**{item} (Code {purchases[item][2]}): Costs {purchases[item][0]}.** *{purchases[item][1]}*'
    await message.channel.send(out)

async def buyItem(id,message,item):
    itemCost = 0
    itemName = ''
    for key in purchases.keys():
        if purchases[key][2] == item.upper():
            itemCost = purchases[key][0]
            itemName = key
    if itemCost == 0:
        await message.channel.send('Item not found')
        return
    userMons = 0
    if id in userCoins.keys():
        userMons = userCoins[id]
    if userMons < itemCost:
        await message.channel.send("You don't have enough Bagridbucks!")
        return
    else:
        userCoins[id] -= itemCost
        userItems[id].append(itemName)
        await message.channel.send(f"You bought the {itemName}! Congratulations!")

        jsonObj = json.dumps(userCoins, indent=4)
        with open('bagridbucks.json','w') as outfile:
            outfile.write(jsonObj)
        jsonObj = json.dumps(userItems, indent=4)
        with open('items.json','w') as outfile:
            outfile.write(jsonObj)

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

    if message.content.lower().startswith('market'):
        await showShop(authorId,message)
        return

    if message.content.lower().startswith('buy'):
        await buyItem(authorId,message,message.content.split(' ')[1])
        return

    bagriddy = False

    for word in message.content.split(' '):
        word = re.sub(r'[^a-zA-Z]', '', word)
        if word.lower() == 'bagrid':
            bagriddy = True
    
    if bagriddy:
        response = random.choice(responses)
        if authorId in userItems.keys():
            if 'Bagrid Confidence Booster' in userItems[authorId]:
                response = f"**{response}**"
        await message.channel.send(response)
        if random.randint(1,10) == 1:
            coinsAdded = giveCoins(authorId)
            await message.channel.send('You earned '+str(coinsAdded)+' BagridBucks!')
            if authorId in userItems.keys():
                if 'Bagrid Doubler' in userItems[authorId]:
                    coinsAdded = giveCoins(authorId)
                    await message.channel.send('A second bagrid appeared! He gives you '+str(coinsAdded)+' BagridBucks!')

client.run(TOKEN)
