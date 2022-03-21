import discord

async def Multipoll (message):
        if message.content.startswith('-multipoll') and message.content.split('\n')[2]:
            if message.content.split('\n')[2]:
                poll1 = message.content.split('\n')[1]
                poll2 = message.content.split('\n')[2]
                emoji1 = ['1️⃣', '2️⃣']
                embed = discord.Embed(
                     title = f'New Poll',
                    description = f'1️⃣ - {poll1}\n 2️⃣ - {poll2}'
                )
                finalSend = await message.channel.send(embed=embed)
                for emoji in emoji1:
                    await finalSend.add_reaction(emoji)

async def Poll (message):
        if message.content.startswith('-poll'):
            poll3 = message.content.split('-poll')[1]
            emoji2 = ['⬆️', '⬇️']
            embed = discord.Embed(
                title = f'New Poll',
                description = f'{poll3}'
            )
            finalSend2 = await message.channel.send(embed=embed)
            for emojis in emoji2:
                await finalSend2.add_reaction(emojis)
        