# To-do list
import database

class To_Do_List:
    def __init__(self):
        self.current_tasks = {}
        self.completed_tasks = {}
        self.base = database.ToDoDatabase()

    def connect_db(self):
        self.base.connect()
        self.base.init_tables()

    def close_db(self):
        self.base.close()

    def register(self, username, password):
        self.user_id = self.base.register_user(username, password)

    def login(self, username, password):
        self.user_id = self.base.login_user(username, password)

    def add_task(self, title, comment = ''):
        if title in self.current_tasks:
            print("Такая задача уже существует!")
        else:
            self.base.add_task(self.user_id, title, comment)
            print("Новая задача создана!")

    def complete_task(self, title):
        if self.base.check_task(self.user_id, title):
            self.base.complete_task(self.user_id, title)
            print("Задача выполнена!")

        else:
            print('Такой задачи не существует или она уже выполнена.')

    def print_current_tasks(self):
        fetch = self.base.get_tasks_of_not_done(self.user_id)
        if not fetch:
            print('Список задач пустой!')
            return

        print(f'Текущие задачи (всего {len(fetch)}):')
        for item in fetch:
            print(f'{item[2]}: {item[3] if item[3] else "(Нет описания)"}')

    def print_completed_tasks(self):
        fetch = self.base.get_tasks_of_done(self.user_id)
        if not fetch:
            print("Список выполненных задач пустой. Вам это ни о чем не говорит? 🙂")
            return

        print(f'Выполненные задачи (всего {len(fetch)})')
        for item in fetch:
            print(f'{item[2]}: {item[3] if item[3] else "(Нет описания)"}')



# инициализация списка и базы данных
l = To_Do_List()
l.connect_db()

print("\n" + "="*40)
print("1. Регистрация")
print("2. Вход")
print("3. Выход")
print("="*40)

flag = 1
while True:
    choice = input("Выберите действие: ")

    if choice == "1":
        username = input("Придумайте логин: ")
        password = input("Придумайте пароль: ")
        l.register(username, password)
        if l.user_id: break

    elif choice == "2":
        username = input("Логин: ")
        password = input("Пароль: ")
        l.login(username, password)
        if l.user_id: break

    elif choice == "3":
        print("До свидания!")
        l.close_db()
        flag = 0
        break

    else:
        print("Неверный выбор!")

if flag:
    print('Для того, чтобы добавить описание задачи, после названия задачи введите ": "')

while flag:
    command = input()

    if command:
        command = command.split(maxsplit=1)
    else:
        print("Пустой ввод!")
        continue

    if len(command) == 1:
        cmd = command[0]
        rest = ''
        title = ''
        comment = ''
    elif len(command) > 1:
        cmd = command[0]
        rest = command[1]
        if ": " in rest:
            title, comment = rest.split(": ", maxsplit=1)
        else:
            title = rest
            comment = ''

    match cmd.lower():
        case "добавить":
            if title:
                l.add_task(title, comment)
            else:
                print("Название не может быть пустым!")

        case "выполнить":
            if title:
                l.complete_task(title)

            else:
                print("Нельзя выполнить пустое задание!")

        case "вывести_текущие":
            if rest:
                print("Лишние аргументы!")
            else:
                l.print_current_tasks()

        case "вывести_выполненные":
            if rest:
                print("Лишние аргументы!")
            else:
                l.print_completed_tasks()

        case "выход":
            if rest:
                print("Лишние аргументы!")
            else:
                print("Выход из приложения")
                print('Все данные сохранены в базе данных)')
                l.close_db()
                break
        case _:
            print("Такой команды не существует!")