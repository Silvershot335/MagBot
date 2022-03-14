import discord

async def modMail(message):
    if message.content.startswith('-modmail') and message.channel.id == (952690676783538277):
        modChannel = client.get_channel(648735556565467146)
        mail = message.content.split('-modmail ')[1]
        submitter = message.author.id
        embed = discord.Embed (
            title = 'New Mod Mail',
            description = f'<@{submitter}>\n{mail}'
    )
    await modChannel.send(embed=embed)