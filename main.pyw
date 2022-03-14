import discord
import os
from help import Help
from mod import modMail
from dotenv import load_dotenv

client = discord.Client()

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.playing, name="-help"))
  print('Alive')

@client.event
async def on_message(message):

  #catch errors I don't understand
  try:
    await modMail(message)
  except:
    print('nope')
  try:
    await Help(message)
  except:
    print('nope')  

  if message.content.startswith('-test'):
    await message.channel.send('reply')

  if message.content.startswith('-playlistrules'):
    await message.reply('https://cdn.discordapp.com/attachments/926538018704195654/950875434554363934/texas.png')

  if message.content.startswith('-playlistlink'):
    await message.reply('https://rates-mocha.vercel.app/')

  if message.content.startswith('good ole silvershot'):
    await message.channel.send('he\'s from texas')


  if message.content.startswith('-killbot') and message.author.id == 177116185006047232:
    await exit()



load_dotenv()
Token = os.environ.get('token')
client.run(Token)

