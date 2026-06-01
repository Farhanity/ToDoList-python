import sqlite3

with sqlite3.connect('todo.db') as conn:
    cur = conn.cursor()

    cur.execute('DROP TABLE tasks')
    cur.execute(''' 
            CREATE TABLE IF NOT EXISTS tasks (
            title TEXT,
            comment TEXT DEFAULT "",
            done INTEGER DEFAULT 0
            )
    ''')


