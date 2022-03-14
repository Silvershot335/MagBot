import discord

async def Help(message):
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