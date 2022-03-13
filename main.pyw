import discord
import os
from dotenv import load_dotenv

client = discord.Client()

@client.event
async def on_ready():
  print('Alive')

@client.event
async def on_message(message):

  if message.content.startswith('!test'):
    await message.channel.send('reply')

  if message.content.startswith('!playlistrules'):
    await message.reply('https://cdn.discordapp.com/attachments/926538018704195654/950875434554363934/texas.png')

  if message.content.startswith('!playlistlink'):
    await message.reply('https://rates-mocha.vercel.app/')

  if message.content.startswith('good ole silvershot'):
    await message.channel.send('he\'s from texas')

load_dotenv()
Token = os.environ.get('token')
client.run(Token)

