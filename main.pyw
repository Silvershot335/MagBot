import discord
import os
from dotenv import load_dotenv

client = discord.Client()

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.playing, name="-help"))
  print('Alive')

@client.event
async def on_message(message):

  if message.content.startswith('-test'):
    await message.channel.send('reply')

  if message.content.startswith('-playlistrules'):
    await message.reply('https://cdn.discordapp.com/attachments/926538018704195654/950875434554363934/texas.png')

  if message.content.startswith('-playlistlink'):
    await message.reply('https://rates-mocha.vercel.app/')

  if message.content.startswith('good ole silvershot'):
    await message.channel.send('he\'s from texas')

  if message.content.startswith('-modmail') and message.channel.id == (952690676783538277):
    modChannel = client.get_channel(648735556565467146)
    mail = message.content.split('-modmail ')[1]
    submitter = message.author.id
    embed = discord.Embed (
      title = 'New Mod Mail',
      description = f'<@{submitter}>\n{mail}'
    )
    await modChannel.send(embed=embed)

  if message.content.startswith('-help'):
    embed = discord.Embed (
      title = 'MagBot',
      description = 'Commands List'
    )
    embed.add_field(
      name = '-playlistrules',
      value = 'Rules for Playlist Club',
      inline=False
    )
    embed.add_field(
      name = '-playlistlink',
      value = 'Playlist Club Website',
      inline=False
    )
    embed.add_field(
      name = '-modmail',
      value = 'Send your messages to the mods.\nUse this command in the Mod Mail channel.\n-modmail Example Text',
      inline=False
    )
    await message.channel.send(embed=embed)

  if message.content.startswith('-killbot') and message.author.id == 177116185006047232:
    await exit()

load_dotenv()
Token = os.environ.get('token')
client.run(Token)

