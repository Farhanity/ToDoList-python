# To-do list

class Task:
    def __init__(self, title, comment):
        self.title = title
        self.comment = comment

    def change_title(self, new_title):
        if self.title != new_title:
            self.title = new_title

    def set_comment(self, comment): # даже если одинаковое описание, можно так делать
        self.comment = comment

    def print_task(self):
        print(self.title, end='')
        if self.comment:
            print(':', self.comment)

    def get_title(self):
        print(self.title)

    def get_comment(self):
        print(self.comment)

    def get_description(self):
        print(f'{self.title}: {self.comment if self.comment else "(Нет описания)"}')

class To_Do_List:
    def __init__(self):
        self.current_tasks = {}
        self.completed_tasks = {}

    def add_task(self, title, comment = ''):
        if title in self.current_tasks:
            print("Такая задача уже существует!")
        else:
            new_task = Task(title, comment)
            self.current_tasks[title] = new_task
            print("Новая задача создана!")

    def complete_task(self, title):
        if title in self.current_tasks:
            completed_task = self.current_tasks.pop(title)
            self.completed_tasks[title] = completed_task
            print("Задача выполнена!")

        else:
            print("Такой задачи не существует или она уже выполнена.")

    def print_current_tasks(self):
        if self.current_tasks:
            print(f'Текущие задачи (всего {len(self.current_tasks)}):')
            for key in self.current_tasks:
                task = self.current_tasks[key]
                task.get_description()
        else:
            print("Список задач пустой!")

    def print_completed_tasks(self):
        if self.completed_tasks:
            print(f'Выполненные задачи (всего {len(self.completed_tasks)})')
            for key in self.completed_tasks:
                task = self.completed_tasks[key]
                task.get_description()
        else:
            print("Список выполненных задач пустой. Вам это ни о чем не говорит? 🙂")


l = To_Do_List()


# идея: выводить рандомные n текущих задач

# добавить вывод описания задания
# добавить изменение задач

print('Для того, чтобы добавить описание задачи, после названия задачи введите ": "')

while True:
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
                break
        case _:
            print("Такой команды не существует!")


