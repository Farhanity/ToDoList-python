import sqlite3

class ToDoDatabase:
    def __init__(self, db_name = 'todo.db'):
        self.name = db_name
        self.conn = None
        self.cur = None

    def connect(self):
        '''Создаем новое соединение'''
        self.conn = sqlite3.connect(self.name)
        self.conn.execute("PRAGMA foreign_keys = ON")
        self.cur = self.conn.cursor()
        return self

    def close(self):
        if self.conn:
            self.conn.close()

    def __enter__(self): # for with ... structure
        return self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def init_tables(self):

        self.cur.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL UNIQUE
                    )
        ''')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                task TEXT NOT NULL,
                comment TEXT NOT NULL DEFAULT "",
                done INTEGER DEFAULT 0,
                FOREIGN KEY (user_id) REFERENCES users(id)
                )
        ''')

        self.conn.commit()
        print('Tables created 🙂')

    def add_user(self, name, password):
        self.cur.execute('INSERT INTO users (username, password) VALUES (?, ?)', (name, password))
        self.conn.commit()

    def get_users(self):
        self.cur.execute('SELECT * FROM users')
        return self.cur.fetchall()

    def add_task(self, user_id, task, comment):
        self.cur.execute('INSERT INTO tasks (user_id, task, comment) VALUES (?, ?,?)', (user_id, task, comment))
        self.conn.commit()

    def get_tasks_not_done(self):
        self.cur.execute('SELECT * FROM tasks WHERE done == 0')
        return self.cur.fetchall()

    def get_tasks_done(self):
        self.cur.execute('SELECT * from tasks WHERE done == 1')

    def complete_task(self, title):
        self.cur.execute('UPDATE tasks SET done = 1 WHERE title LIKE "?"', (title))

    def get_tasks_of(self, user_id):
        self.cur.execute('SELECT * FROM tasks WHERE user_id == ?', (user_id,))
        return self.cur.fetchall()

if __name__ == '__main__':
    with ToDoDatabase() as db:
        db.init_tables()

        db.add_user('farhat', 'Fa050505__')
        db.add_user('aaa', 'sdjfllsjf')

        db.add_task(1, 'aaa', '')
        db.add_task(2, 'hellp', 'by')
        db.add_task(1, 'hiii', 'bye')

        print(db.get_tasks_of(1))