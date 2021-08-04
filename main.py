import discord
import os
#from dotenv import load_dotenv

#load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if client.user.mentioned_in(message):
        if 'teşekkür' in message.content:
            await message.channel.send('Rica ederim')
        elif 'nasılsın' in message.content:
            await message.channel.send('İyiyim teşekkür ederim siz nasılsınız?')
        else:
            await message.channel.send('Buyrun benim?')

client.run(os.getenv('DC_TOKEN'))