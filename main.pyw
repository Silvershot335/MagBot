import discord
import os
import sqlite3
from help import Help
from commands import add_Command
from commands import checkCommands
from mod import modMail
from poll import Poll
from poll import Multipoll
from dotenv import load_dotenv

client = discord.Client()

banned = ['testvar2', 'nigger', 'faggot', 'nigga', ]


@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.playing, name="-help"))
  print('Alive')

@client.event
async def on_message(message):

  for x in banned: 
    if message.content.casefold().find(x) >= 0:
      mute = discord.utils.get(message.guild.roles, name = "Muted")
      await message.reply('<@&648751890045206568> Chat Filter Tripped')
      await message.author.add_roles(mute)
      await message.delete()

    #catch errors I don't understand
  if message.content.startswith('-modmail') and message.channel.id == (952690676783538277):
    try:
      await modMail(message)
    except Exception as e:
      print(e)
  if message.content.startswith('-help'):
    try:
      await Help(message)
    except Exception as e:
      print(error)  
  if message.content.startswith('-multipoll'):
    try:
      await Multipoll(message)
    except Exception as e:
      print(e)
  if message.content.startswith('-poll'):
    try:
      await Poll(message)
    except Exception as e:
      print(e)
  if message.content.startswith('-addcommand'):
    try:
      await add_Command(message)
    except Exception as e:
      print(e)
  if message.content.startswith('-key'):
    try:
      await checkCommands(message)
    except Exception as e:
      print(e)



  if message.content.startswith('-test'):
    await message.channel.send('reply')

  if message.content.startswith('-playlistrules'):
    await message.reply('https://cdn.discordapp.com/attachments/926538018704195654/950875434554363934/texas.png')

  if message.content.startswith('-playlistlink'):
    await message.reply('https://rates-mocha.vercel.app/')

  if message.content.startswith('good ole silvershot'):
    await message.channel.send('he\'s from texas')


  if message.content.startswith('-killbot') and message.author.id == 177116185006047232:
    await message.reply('oof')
    await exit()



load_dotenv()
Token = os.environ.get('token')
client.run(Token)

