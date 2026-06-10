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
        # self.cur.execute('DROP TABLE IF EXISTS tasks')
        # self.cur.execute('DROP TABLE IF EXISTS users')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
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

    def get_users(self):
        self.cur.execute('SELECT * FROM users')
        return self.cur.fetchall()

    def add_task(self, user_id, task, comment = ''):
        self.cur.execute('INSERT INTO tasks (user_id, task, comment) VALUES (?, ?, ?)', (user_id, task, comment))
        self.conn.commit()

    def get_tasks_not_done(self):
        self.cur.execute('SELECT * FROM tasks WHERE done == 0')
        return self.cur.fetchall()

    def get_tasks_done(self):
        self.cur.execute('SELECT * from tasks WHERE done == 1')

    def complete_task(self, user_id, title):
        self.cur.execute('UPDATE tasks SET done = 1 WHERE task LIKE ? AND user_id == ?', (title, user_id))

    def get_tasks_of_not_done(self, user_id):
        self.cur.execute('SELECT * FROM tasks WHERE user_id == ? and done == 0', (user_id,))
        return self.cur.fetchall()

    def get_tasks_of_done(self, user_id):
        self.cur.execute('SELECT * FROM tasks WHERE user_id == ? and doen == 1', (user_id,))
        return self.cur.fetchall()

    def register_user(self, username, password):
        """Регистрация нового пользователя"""
        # Проверяем, что поля не пустые
        if not username or not password:
            print("Логин и пароль обязательны!")
            return None

        # Проверяем, не занят ли username
        self.cur.execute('SELECT id FROM users WHERE username = ?', (username,))
        if self.cur.fetchone():
            print(f"Пользователь '{username}' уже существует!")
            return None

        try:
            # Создаём нового пользователя
            self.cur.execute(
                'INSERT INTO users (username, password) VALUES (?, ?)',
                (username, password)
            )
            self.conn.commit()
            user_id = self.cur.lastrowid
            print(f"Регистрация успешна! Ваш ID: {user_id}")
            return user_id
        except Exception as e:
            print(f"Ошибка регистрации: {e}")
            return None

    def login_user(self, username, password):
        """Авторизация пользователя"""
        # Проверяем, что поля не пустые
        if not username or not password:
            print("Логин и пароль обязательны!")
            return None

        # Ищем пользователя
        self.cur.execute(
            'SELECT id FROM users WHERE username = ? AND password = ?',
            (username, password)
        )
        user = self.cur.fetchone()

        if user:
            print(f"Добро пожаловать, {username}!")
            return user[0]  # Возвращаем id
        else:
            print("Неверный логин или пароль!")
            return None

if __name__ == '__main__':
    with ToDoDatabase() as db:
        db.init_tables()

        id1 = db.register_user('farhat', 'Fa050505__')
        print(id1)