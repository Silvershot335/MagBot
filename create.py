import sqlite3


def create():
    conn = None
    try:
        conn = sqlite3.connect('./Databases/BotCommands.db')
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def table(conn, sql):
    cur = conn.cursor()
    cur.execute(sql)

def main():
    database = './databases/BotCommands.db'

    sql_create_testing_table = """ CREATE TABLE IF NOT EXISTS BotCommands (
                                    id integer PRIMARY KEY,
                                    key text NOT NULL,
                                    value text NOT NULL
    );"""

    conn = create(database)

    if conn is not None:
        table(conn, sql_create_testing_table)
    else:
        print('Error! You did the BIG DUMB!')

if  __name__ == '__main__':
    main()


