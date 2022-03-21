import discord
import sqlite3
from create import create

async def add_Command(message):
    if message.content.startswith('-addcommand'):
        try:
            key = message.content.split('\n')[1]
            value = message.content.split('\n')[2]
        except:
            await message.reply('You Fucked Up')
        else:
            insertCommand(key, value)    
            await message.reply('Command Added!')

async def checkCommands(message):
    if message.content.startswith('-key'):
        try:
            key = message.content.split('\n')[1]
        except:
            await message.reply('You Fucked Up')
        else:
            rows = fetchCommand(key)
            await message.channel.send(rows[2])

def insertCommand(key, value):
    conn = create()
    with conn:
        command = (key, value)
        CommandInput(conn, command)

def CommandInput(conn, command):
    sql = '''INSERT INTO BotCommands(key,value)
                VALUES(?,?)'''
    cur = conn.cursor()
    cur.execute(sql, command)
    conn.commit()
    return cur.lastrowid

def fetchCommand(key):
    conn = create()
    with conn:
        return fetchData(conn, key)

def fetchData(conn, key):
    sql = 'SELECT * FROM BotCommands WHERE key=?'
    cur = conn.cursor()
    cur.execute(sql, [key])
    rows = cur.fetchone()
    return rows