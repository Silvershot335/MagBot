import sqlite3


def create():
    conn = None
    try:
        conn = sqlite3.connect('./Databases/BotCommands.db')
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn


